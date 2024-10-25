using System;
using System.Configuration;
using System.Data.SqlClient;
using System.IO.Ports;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

namespace RaspberryServertest
{
    internal class Program
    {
        static SerialPort _serialPort;
        static string temperature = "0";
        static string lightStatus = "0";
        static string alarmLightStatus = "0";
        static string buttonStatus = "0";
        static int readInterval = 400;

        static bool buttonAlarmActive = false;
        static bool temperatureAlarmActive = false;
        static bool temperatureAlarmAcknowledged = false;
        static double temperatureLimit = 23;
        public static int Main(string[] args)
        {
            Console.WriteLine("Server: Hello!");
            Thread serverThread = new Thread(() => StartServer());
            Thread readThread = new Thread(() => Read());
            Thread checkAlarmsThread = new Thread(() => CheckAlarmsFromSQL());

            Console.Write("Use default settings for Arduino? Y/N:");
            string defaultSetting = Console.ReadLine();
            string port, baudrate;
            if (defaultSetting == "Y")
            {
                port = "/dev/ttyACM0";
                baudrate = "9600";
                Console.WriteLine("Using port: " + port + ", baudrate: " + baudrate);
            }
            else
            {
                Console.Write("Port:");
                port = Console.ReadLine();
                Console.Write("Baudrate:");
                baudrate = Console.ReadLine();
            }

            // create a SerialPort on port COM#
            _serialPort = new SerialPort(port, int.Parse(baudrate));

            // set the read/write timeouts
            _serialPort.ReadTimeout = 1500;
            _serialPort.WriteTimeout = 1500;
            _serialPort.Open();
            readThread.Start();
            //checkAlarmsThread.Start(); //not in use, functionality moved to Forms program
            StartServer();

            _serialPort.Close();
            return 0;
        }

        public static void StartServer()
        {
            IPAddress ipAddress = IPAddress.Parse("192.168.247.55");
            IPEndPoint localEndPoint;
            
            Console.WriteLine("Try host on eth0 or wlan0? or custom IP (ip)?");
            string hostChoice = Console.ReadLine();
            if (hostChoice == "eth0")
            {
                Console.WriteLine("Trying host ip 192.168.97.55 (should be eth0)");
                ipAddress = IPAddress.Parse("192.168.97.55");
            }
            else if (hostChoice == "wlan0")
            {
                Console.WriteLine("Trying host ip 192.168.11.3 (should be wlan0)");
                ipAddress = IPAddress.Parse("192.168.11.3");
            }
            else if (hostChoice == "ip")
            {
                string ipCustom = Console.ReadLine();
                try
                {
                    ipAddress = IPAddress.Parse(ipCustom);
                }
                catch (Exception)
                {
                    Console.WriteLine("IP rejected, written wrong");
                }
            }
            else { Console.WriteLine("Command not recognized"); }

            try
            {
                //Socket Tcp protocol listening for 10 request at a time
                localEndPoint = new IPEndPoint(ipAddress, 11800);
                Socket listener = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
                listener.Bind(localEndPoint);
                listener.Listen(10);

                while (true)
                {
                    Console.WriteLine("Waiting for a connection...");
                    Socket handler = listener.Accept();

                    // Client data
                    string data = null;
                    byte[] bytes = null;

                    while (true)
                    {
                        bytes = new byte[1024];
                        int bytesRec = handler.Receive(bytes);
                        data += Encoding.ASCII.GetString(bytes, 0, bytesRec);
                        if (data.IndexOf("<EOF>") > -1)
                        {
                            break;
                        }
                    }

                    Console.WriteLine("Command received : {0}", data);

                    // Reply
                    //byte[] msg = Encoding.ASCII.GetBytes("Sensor value 20");
                    byte[] msg = DataResponse(data.ToString());
                    handler.Send(msg);
                    handler.Shutdown(SocketShutdown.Both);
                    handler.Close();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
            //Console.WriteLine("\n Press any key to continue...");
            //Console.ReadKey();
        }

        public static byte[] DataResponse(string data)
        {
            byte[] response = null;
            if (data == "GET BUTTON<EOF>")
            {
                response = Encoding.ASCII.GetBytes(buttonStatus);
            }
            else if (data == "GET TEMPERATURE<EOF>")
            {
                response = Encoding.ASCII.GetBytes(temperature);
            }
            else if (data == "GET LIGHT<EOF>")
            {
                response = Encoding.ASCII.GetBytes(lightStatus);
            }
            else if (data == "GET ALARMLIGHT<EOF>")
            {
                response = Encoding.ASCII.GetBytes(alarmLightStatus);
            }
            else if (data == "TOGGLE DIODE<EOF>")
            {
                _serialPort.Write("L");
                response = Encoding.ASCII.GetBytes("diode toggled");
            }
            else if (data == "INC TEMPERATURELIMIT<EOF>")
            {
                temperatureLimit += 1;
                response = Encoding.ASCII.GetBytes(temperatureLimit.ToString());
            }
            else if (data == "DEC TEMPERATURELIMIT<EOF>")
            {
                temperatureLimit -= 1;
                response = Encoding.ASCII.GetBytes(temperatureLimit.ToString());
            }
            else if (data == "ACK TEMPERATUREALARM<EOF>")
            {
                temperatureAlarmAcknowledged = true;
                response = Encoding.ASCII.GetBytes("Acknowledged temperature above limit");
            }
            else if (data == "ALARM OFF<EOF>")
            {
                _serialPort.Write("O");
                temperatureAlarmActive = false;
                //Console.WriteLine("Alarms Cleared");
                response = Encoding.ASCII.GetBytes("no alarms");
            }
            else if (data == "ALARM ON<EOF>")
            {
                _serialPort.Write("A");
                //Console.WriteLine("Alarm light on");
                response = Encoding.ASCII.GetBytes("in fact, there are alarms");
            }
            else
            {
                Console.WriteLine("Command not understood");
                response = Encoding.ASCII.GetBytes("Default response");
            }

            return response;
        }

        public static void Read()
        {
            ClearSerialBuffer();
            int i = 0;
            int buttonPressedForIntervals = 0;
            while (true)
            {
                try
                {
                    string message = _serialPort.ReadLine();
                    //Console.WriteLine(message);
                    string[] serialData = message.Split(';');
                    if (serialData.Length > 1)
                    {
                        temperature = serialData[0];
                        lightStatus = serialData[1];
                        alarmLightStatus = serialData[2];
                        buttonStatus = serialData[3];
                    }

                    //Alarm if button pressed too long
                    if (Convert.ToUInt32(buttonStatus) == 1)
                    {
                        buttonPressedForIntervals++;
                    }
                    else if (Convert.ToUInt32(buttonStatus) == 0)
                    {
                        buttonPressedForIntervals = 0;
                        buttonAlarmActive = false;
                    }
                    if ((buttonPressedForIntervals > (1000/readInterval)*10) && !buttonAlarmActive)
                    {
                        Console.WriteLine("DOOR HELD OPEN FOR MORE THAN 10 SEC");
                        PostAlarmToSQL("BUTTON");
                        buttonAlarmActive = true;
                    }

                    //Alarm if temperature too high
                    if ((Convert.ToDouble(temperature) > temperatureLimit) && !temperatureAlarmActive)
                    {
                        Console.WriteLine("TEMPERATURE ABOVE LIMIT");
                        PostAlarmToSQL("TMP");
                        temperatureAlarmActive = true;
                        temperatureAlarmAcknowledged = false;
                    }
                    else if ((Convert.ToDouble(temperature) < temperatureLimit) && temperatureAlarmAcknowledged)
                    {
                        temperatureAlarmActive = false;
                    }

                    //Clear serial buffer when too many lines accumulated (when raspberry reads slower than arduino)
                    if (i > 50)
                    {
                        ClearSerialBuffer();
                        i = 0;
                    }
                    i++;

                }
                catch (TimeoutException)
                {
                    //Console.WriteLine("Timeout..");
                }
                Thread.Sleep(readInterval);
            }
        }

        public static void ClearSerialBuffer()
        {
            while (_serialPort.BytesToRead > 0)
            {
                _serialPort.ReadByte();
            }
            //Console.WriteLine("Serial buffer cleared");
        }


        static void PostAlarmToSQL(string alarmType)
        {
            
            string sqlQuery = $@"INSERT INTO ALARM VALUES ('NA','NA','2069-09-30','Error in PostAlarmToSQL')";
            if (alarmType == "TMP")
            {
                sqlQuery = $@"INSERT INTO ALARM (AlarmCat, AlarmCode, AlarmMessage) VALUES (2,'TH','Temperature above limit')";
            }
            else if (alarmType == "BUTTON")
            {
                sqlQuery = $@"INSERT INTO ALARM (AlarmCat, AlarmCode, AlarmMessage) VALUES (5,'DS','DOOR STUCK!!!')";
            }
            
            try
            {
                string conn = ConfigurationManager.ConnectionStrings["conn"].ConnectionString;
                SqlConnection conFood = new SqlConnection(conn);
                SqlCommand sql = new SqlCommand(sqlQuery, conFood);
                conFood.Open();
                sql.ExecuteNonQuery();
                conFood.Close();
                Console.WriteLine("Alarm posted");
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

        //NOT IN USE
        static void CheckAlarmsFromSQL()
        {
            while (true)
            {
                try
                {
                    string sqlQuery = $@"SELECT * FROM ALARM";
                    string conn = ConfigurationManager.ConnectionStrings["conn"].ConnectionString;
                    SqlConnection conFood = new SqlConnection(conn);
                    SqlCommand sql = new SqlCommand(sqlQuery, conFood);
                    conFood.Open();
                    SqlDataReader dataReader = sql.ExecuteReader();
                    string retrievedTableValue = "";
                    while (dataReader.Read() == true)
                    {
                        retrievedTableValue = dataReader[0].ToString();
                    }
                    conFood.Close();
                    if (retrievedTableValue.Length > 0 )
                    {
                        Console.WriteLine("No alarms");
                        temperatureAlarmActive = false;
                        _serialPort.Write("O");
                    }
                    else
                    {
                        Console.WriteLine("Alarms are pending");
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
                Thread.Sleep(3000);
            }
        }
    }
}
