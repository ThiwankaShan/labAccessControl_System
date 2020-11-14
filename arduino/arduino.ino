#include <SPI.h>
#include <RFID.h>
#define SS_PIN 10
#define RST_PIN 9
RFID rfid(SS_PIN, RST_PIN);
String rfidCard;

#include <Servo.h>
int servoPin = 3; 
Servo Servo1;

int buzzer = 8;
 
String acess;

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.init();

  Servo1.attach(servoPin); 
  
}

void loop() {
  Serial.println("main loop");
  while (true){
     if (rfid.isCard()) {
      if (rfid.readCardSerial()) {
      rfidCard = String(rfid.serNum[0]) + " " + String(rfid.serNum[1]) + " " + String(rfid.serNum[2]) + " " + String(rfid.serNum[3]);
      Serial.println(rfidCard);
      break;
      
      }
      rfid.halt();
    }
    
    }
  
 
      

      while(!Serial.available()){}
      acess = Serial.readStringUntil('\n');
     
      if (acess.equals("granted")){
        Servo1.write(90); 
        delay(5000);
        Servo1.write(0); 
        }
      else if (acess.equals("denied")){
        tone(buzzer,500,500);
        delay(1000);
        }

        acess='#';
         
       
  
}
