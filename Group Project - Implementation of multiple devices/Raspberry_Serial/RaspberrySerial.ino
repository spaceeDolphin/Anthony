const int sensorPin = A0;
const int buttonPin = 7;
const int redDiodePin = 8;
const int greenDiodePin = 9;

const float baselineTemp = 19.0;
int lastButtonState = HIGH;
int currentButtonState;
bool diodeToggle = false;
bool alarm = false;
bool doorOpen = false;

void setup() {
  // put your setup code here, to run once:
  pinMode(buttonPin, INPUT_PULLUP); //LOW when switch is closed
  pinMode(redDiodePin, OUTPUT);
  digitalWrite(redDiodePin, LOW);
  pinMode(greenDiodePin, OUTPUT);
  digitalWrite(greenDiodePin, LOW);
  Serial.begin(9600);
}

void loop() {
  currentButtonState = digitalRead(buttonPin);
  if(lastButtonState == LOW && currentButtonState == HIGH)
  {
    //Serial.println("DOORCLOSED");
    //diodeToggle = !diodeToggle;
  }
  else if(lastButtonState == HIGH && currentButtonState == LOW)
  {
    //Serial.println("DOOROPEN");
  }
  lastButtonState = currentButtonState;

  if(currentButtonState == LOW)
  {
    doorOpen = true;
  }
  else if (currentButtonState == HIGH)
  {
    doorOpen = false;
  }

  if(Serial.available() > 0)
  {
    char command = Serial.read();
    if(command == 'L')
    {
      diodeToggle = !diodeToggle;
    }
    else if (command == 'A')
    {
      digitalWrite(redDiodePin, HIGH);
      alarm = true;
    }
    else if (command == 'O')
    {
      digitalWrite(redDiodePin, LOW);
      alarm = false;
    }
  }
  
  if(diodeToggle)
    {
      digitalWrite(greenDiodePin, HIGH);
    }
    else
    {
      digitalWrite(greenDiodePin, LOW);
    }

  //** TEMPERATURE SENSOR **//
  int sensorVal = analogRead(sensorPin);
  //Serial.print("Sensor Value:");
  //Serial.print(sensorVal);

  // convert ADC reading to voltage
  float voltage = (sensorVal/1024.0)*5.0;
  //Serial.print(",Volts:");
  //Serial.print(voltage);
  //Serial.print(",degrees C:");

  // convert voltage to temperature in degrees C
  float temperature = (voltage-.5)*100;
  Serial.print(temperature);
  Serial.print(";");
  Serial.print(diodeToggle);
  Serial.print(";");
  Serial.print(alarm);
  Serial.print(";");
  Serial.println(doorOpen);

  delay(500);
}
