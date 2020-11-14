#include <SPI.h>
#include <RFID.h>
#define SS_PIN 10
#define RST_PIN 9
RFID rfid(SS_PIN, RST_PIN);
String rfidCard;

#include <Servo.h>
int servoPin = 3;
int open_door = 90;
int close_door = 0;
Servo Servo1;

int buzzer = 8;

String acess;

void setup()
{
  Serial.begin(9600);
  SPI.begin();
  rfid.init();

  Servo1.attach(servoPin);
  Servo1.write(close_door);
}

void loop()
{

  while (true)
  {

    if (rfid.isCard())
    {

      if (rfid.readCardSerial())
      {

        rfidCard = String(rfid.serNum[0]) + " " + String(rfid.serNum[1]) + " " + String(rfid.serNum[2]) + " " + String(rfid.serNum[3]);
        Serial.println(rfidCard);
        break;
      }

      rfid.halt();
    }
  }

  while (!Serial.available())
  {
  }
  acess = Serial.readStringUntil('\n');

  if (acess.equals("granted"))
  {

    Servo1.write(open_door);
    delay(8000);
    Servo1.write(close_door);
  }
  else if (acess.equals("denied"))
  {

    tone(buzzer, 500, 500);
    delay(1000);
  }

  acess = '#';
}
