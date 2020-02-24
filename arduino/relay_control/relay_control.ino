int relay = 13;

void setup() 
{
  pinMode(relay,OUTPUT);
  Serial.begin(115200);
  delay(100);
}


void loop() 
{
digitalWrite(relay,HIGH);
Serial.print("\nPulled High");
delay(120000); //2 mins on
digitalWrite(relay,LOW);
Serial.print("\nDropped Low");
delay(20000); // 20 seconds off 
}
