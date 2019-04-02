/* ArduinoESP module
Interfacing ESP with Arduino

REQUIREMENTS
    SoftwareSerial.h
 */    

//#include "SoftwareSerial.h"
//SoftwareSerial ESPserial(0, 1); // RX | TX

void arduinoESPSetup()
{
    Serial.begin(115200);
	  //ESPserial.begin(9600);
}
