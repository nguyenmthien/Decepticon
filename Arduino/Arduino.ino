/*MAIN PROGRAM
Created 20190319
Last edited 20190320
*/
<<<<<<< HEAD
#include <WiFi.h>
#include <esp_wifi.h>
WiFiServer wifiServer(23); // communication port
=======

>>>>>>> 629f22185dfd82fe905ec42d02f7f8de8d9b9665

// Wifi id and password
  const char* ssid = "nguyenmthien";
  const char* password = "299792458";

// define client
WiFiClient client = wifiServer.available();
  // esp ip 
  IPAddress ip(192, 168, 137, 128); 
  IPAddress subnet(255, 255, 255, 0);
  IPAddress gw(192, 168, 1, 1);
//DEFINE PINS
int leftMotorIN1 = 15, leftMotorIN2 = 2,
    rightMotorIN1 = 16, rightMotorIN2 = 17,
    leftMotorPWM = 4, rightMotorPWM = 5 ;

//DEFINE GLOBAL VARIABLES
double omegal = 0, omegar = 0;

unsigned long tau = 1, previoustau = 0, dtau = 1;
unsigned long t = 1, previoust = 0;
double theta = 0;
double PVl, PVr, SPl, SPr, El, Er, Ul, Ur;
double previousIl, previousIr;
double previousEl, previousEr;

int speedCount = 0;

int input;

bool debug = true;

bool leftMotorIN1Bool = 0, leftMotorIN2Bool = 0,
     rightMotorIN1Bool = 0, rightMotorIN2Bool = 0;

//ERROR FUNCTION & PID VARIABLES
double k1[3] = {50, 100, 150};
double k2[3] = {50, 100, 150};
double Kp = 10.0, Ki = 0.0, Kd = 0.0;


//IMPORT MODULES
#include "arduino_esp.h"
#include "interrupt.h"
#include "pid.h"
#include "dictionary.h"
#include "interpreter.h"
#include "L298N.h"
#include "WifiSetup.h"
#include "ESP.h"

void setup()
{
  WifiSetup();
    
	L298NSetup();
	
	interruptSetup();
}
void loop()
{
  SocketServer();
}
