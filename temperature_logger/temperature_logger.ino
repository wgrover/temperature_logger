// MAX6675  Arduino
// SO	      pin 4 MISO
// CS	      pin 5 CS
// SCK	    pin 6 CLK
// VCC	    5V
// GND	    GND

#include "max6675.h"
int thermoDO = 4;
int thermoCS = 5;
int thermoCLK = 6;
MAX6675 thermocouple(thermoCLK, thermoCS, thermoDO);

void setup() {
  Serial.begin(115200);
  delay(500);  // wait for MAX chip to stabilize
}

void loop() {  
  Serial.println("X" + String(thermocouple.readCelsius()) + "Y");
  delay(1000);    //  must delay AT LEAST 250ms between reads!
}
