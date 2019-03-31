/*MAIN PROGRAM
Created 20190319
Last edited 20190320
*/
#include <ESP8266WiFi.h>

WiFiServer wifiServer(23); // communication port

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
const int leftMotorIN1 = 13, leftMotorIN2 = 15,
          rightMotorIN1 = 3, rightMotorIN2 = 1,
          leftMotorPWM = 14, rightMotorPWM = 12 ;

//DEFINE GLOBAL VARIABLES
double omegal = 0, omegar = 0;
unsigned long tau = 1, previoustau = 0, dtau = 1;
unsigned long t = 1, previoust = 0;
double theta = 0;
double PVl, PVr, SPl, SPr, El, Er, Ul, Ur;
double previousIl, previousIr;
double previousEl, previousEr;

int speedCount = 0;

char input;   // input is char because client read can only read char

bool debug = true;

bool leftMotorIN1Bool = 0, leftMotorIN2Bool = 0,
     rightMotorIN1Bool = 0, rightMotorIN2Bool = 0;

//ERROR FUNCTION & PID VARIABLES
double k1[3] = {50, 100, 150};
double k2[3] = {50, 100, 150};
double Kp = 10.0, Ki = 0.0, Kd = 0.0;


//IMPORT MODULES
#include "interrupt.h"
#include "pid.h"
#include "dictionary.h"
#include "interpreter.h"
#include "L298N.h"
#include "WifiSetup.h"
#include "SocketServer.h"


void setup()
{
  WifiSetup();
  
	L298NSetup();
	
	interruptSetup();
}

void loop()
{   
  SocketServer();
    
//  if (!debug)
//  {
//    PID();
//  }
//    
//  L298NMotorDriver();
}
