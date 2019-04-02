/* ArduinoESP module
Interfacing ESP with Arduino

REQUIREMENTS
    SoftwareSerial.h
 */    

<<<<<<< HEAD:Arduino/ESP.h
  if (client) {
 
    while (client.connected()) {   // while the client is still connected do:
      String strInput = "";        // strInput is a string that will be appended     
      while (client.available()) {      // while there are still datas sent to the client do:
          input = client.read() ;     // read the char type input from client and 
          strInput.concat(input);  // concat: append remaining character from input to strInput String 
      }                     
      int intInput = strInput.toInt();  // convert the strInput String into integer 
      interprete(intInput, client);   // interprete function with two variable intInput and client 
      if (!debug)
      {
        PID();
      }
    
      L298NMotorDriver();
      delay(0.01);
    }
  }
=======
//#include "SoftwareSerial.h"
//SoftwareSerial ESPserial(0, 1); // RX | TX

void arduinoESPSetup()
{
    Serial.begin(115200);
	  //ESPserial.begin(9600);
>>>>>>> 629f22185dfd82fe905ec42d02f7f8de8d9b9665:Arduino/arduino_esp.h
}
