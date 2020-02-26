#include <stdint.h>
int relay = 13;

void setup() 
{
  pinMode(relay,OUTPUT);
  Serial.begin(115200);
  delay(100);
}


void loop() 
{
  while(1) {
    if (Serial.available() > 0 )
  
  {
    int in_byte = Serial.read();

     switch (in_byte)
     {
      case 'y':
        digitalWrite(relay,HIGH);
        Serial.print("\nPulled High");       
        break;

      case 'n':
        digitalWrite(relay,LOW);
        Serial.print("\nPulled Low");
        break;

      /*default:
        digitalWrite(relay,HIGH);
        Serial.print("\nPulled High");
        delay(120000); //2 mins on
        digitalWrite(relay,LOW);
        Serial.print("\nDropped Low");
        delay(20000); // 20 seconds off
      */
     }
  }
 }
 
}
