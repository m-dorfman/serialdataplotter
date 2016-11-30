#include "Arduino.h"

void setup()
{
  // initialize serial comms
  Serial.begin(115200); 
}

void loop()
{
  // read A0
  int val1 = analogRead(0);

  // print to serial
  Serial.println(val1);

  // wait 
  delay(50);
}