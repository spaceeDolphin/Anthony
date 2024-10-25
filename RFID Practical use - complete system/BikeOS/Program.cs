using BikeOS;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Drawing.Text;
using System.Linq;

Vehicle vehicle;
string databaseConfig = ConfigurationManager.ConnectionStrings["BikeShare"].ConnectionString;
int stationId, bikeId;
stationId = 1;

//Initialization
string getStationsSqlQuery = @"SELECT StationId, StationName FROM BIKE_STATION";
string getBikeSqlQuery = @"SELECT BikeId, BikeName FROM BIKE";
string getTagsSqlQuery = @"SELECT RFID FROM ViewRegisteredTags";
GetLists(getStationsSqlQuery, out List<int> stationIdList, out List<string> stationNameList);
GetLists(getBikeSqlQuery, out List<int> bikeIdList, out List<string> bikeNameList);

Console.WriteLine("Initializing...");
WriteLogo();
Console.WriteLine("Available stations:");
ShowLists(stationIdList, stationNameList);
Console.WriteLine();
Console.WriteLine("Available bikes:");
ShowLists(bikeIdList, bikeNameList);
Console.WriteLine();
Console.WriteLine("Select bike by index ...");
bikeId = Convert.ToInt32(Console.ReadLine());
vehicle = new Bike(bikeId);
vehicle.Name = bikeNameList[vehicle.Id - 1];
GetLastStation(vehicle.Id);
Console.WriteLine("Bike " + vehicle.Id.ToString() + " - " + vehicle.Name + " selected.");
Console.WriteLine("Last location: " + stationNameList[stationId - 1]);
Console.WriteLine("Running logger...");
Console.ReadLine();
Logger();
Console.WriteLine("Shutting down...");
Console.ReadLine();

string GetStation()
{
    string stationName;
    Console.WriteLine();
    Console.WriteLine("Available stations:");
    ShowLists(stationIdList, stationNameList);
    Console.WriteLine();
    Console.WriteLine("Select station by index ...");
    stationId = Convert.ToInt32(Console.ReadLine());
    stationName = stationNameList[stationId - 1];
    return stationName;
}

void GetLastStation(int bikeId)
{
    string sqlQuery = 
        @$"SELECT TOP 1 BS.StationId 
        FROM BIKE_LOCK AS BL, BIKE_STATION AS BS
        WHERE BS.StationId = BL.StationId
        AND BikeId = {bikeId}
        ORDER BY LockTime DESC;";
    try
    {
        int retrievedInt;
        //string retrievedString;
        SqlConnection connDatabase = new SqlConnection(databaseConfig);
        SqlCommand sql = new SqlCommand(sqlQuery, connDatabase);
        connDatabase.Open();
        SqlDataReader dr = sql.ExecuteReader();
        while (dr.Read())
        {
            retrievedInt = dr.GetInt32(0);
            //retrievedString = dr.GetString(1);
            stationId = retrievedInt;
        }
        connDatabase.Close();
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
        Console.WriteLine("Setting location to standard: USN Nord");
        stationId = 1;
    }
}

void GetLists(string sqlQuery, out List<int> idList, out List<string> nameList)
{
    idList = new List<int>();
    nameList = new List<string>();
    try
    {
        int retrievedInt;
        string retrievedString;
        SqlConnection connDatabase = new SqlConnection(databaseConfig);
        SqlCommand sql = new SqlCommand(sqlQuery, connDatabase);
        connDatabase.Open();
        SqlDataReader dr = sql.ExecuteReader();
        while (dr.Read())
        {
            retrievedInt = dr.GetInt32(0);
            retrievedString = dr.GetString(1);
            idList.Add(retrievedInt);
            nameList.Add(retrievedString);
        }
        connDatabase.Close();
        Console.WriteLine("List imported successfully");
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
}
void ShowLists(List<int> idList, List<string> nameList)
{
    for (int i = 0; i < idList.Count; i++)
    {
        int id = idList[i];
        string name = nameList[i];
        Console.WriteLine(id + " - " + name);
    }
}

bool CheckIfTagIsInDb(string sqlQuery, string tagId)
{
    bool result = false;
    try
    {
        string retrievedString;
        SqlConnection connDatabase = new SqlConnection(databaseConfig);
        SqlCommand sql = new SqlCommand(sqlQuery, connDatabase);
        connDatabase.Open();
        SqlDataReader dr = sql.ExecuteReader();
        while (dr.Read())
        {
            retrievedString = dr.GetString(0);
            if (retrievedString == tagId)
            {
                result = true;
            }
        }
        connDatabase.Close();
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
    return result;
}

void WriteLogo()
{
    Console.WriteLine(" ____    _   _               ____     _____");
    Console.WriteLine("|  _ \\  (_) | |             / __ \\   / ____|");
    Console.WriteLine("| |_) |  _  | | __   ___   | |  | | | (___");
    Console.WriteLine("|  _ <  | | | |/ /  / _ \\  | |  | |  \\___ \\");
    Console.WriteLine("| |_) | | | |   <  |  __/  | |__| |  ____) |");
    Console.WriteLine("|____/  |_| |_|\\_\\  \\___|   \\____/  |_____/");
    Console.WriteLine();
}

void Logger()
{
    string tagId, bikeStatus;
    int loopLimit = 100;
    int iLoop = 0;
    while (iLoop <= loopLimit)
    {
        Console.Clear();
        WriteLogo();
        //Tid kun for estetikk. Tid til loggføring hentes i database i stored procedure
        DateTime dateTime = DateTime.Now;
        Console.WriteLine("Current time: " + dateTime.ToString());
        Console.WriteLine("Bike: " + vehicle.Name);
        Console.WriteLine("Awaiting RFID... (or Q to Quit)");
        tagId = Console.ReadLine();
        if ((tagId == "q") || (tagId == "Q")) { break; }
        if (CheckIfTagIsInDb(getTagsSqlQuery, tagId))
        {
            BikeToggle bike = new BikeToggle(tagId, vehicle.Id, stationId);
            bikeStatus = bike.GetBikeStatus();
            if (bikeStatus == "Locked")
            {
                bike.RegisterUnlock();
                Console.WriteLine("Registered unlock with RFID " + tagId);
            }
            else if (bikeStatus == "Unlocked")
            {
                string currentStation;
                currentStation = GetStation();
                bike.StationId = stationId;
                bike.RegisterLock();
                Console.WriteLine("Registered lock at " + currentStation + " with RFID " + tagId);
            }
        }
        else
        {
            Console.WriteLine("Invalid tag; "+tagId+" is not a registered tag");
        }
        iLoop++;
        Thread.Sleep(2500);
    }
}