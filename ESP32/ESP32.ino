/*MAIN PROGRAM
Created 20190319
Last edited 20130402
*/


#include <WiFi.h>
#include <esp_wifi.h>

const char* ssid     = "nguyenmthien";
const char* password = "299792458";
IPAddress ip(192, 168, 137, 128); 
IPAddress subnet(255, 255, 255, 0);
IPAddress gw(192, 168, 1, 1);
/* create a server and listen on port 23 */
WiFiServer server(23);
WiFiClient client;
//WiFiServer debugServer(32);
//WiFiClient debugClient;



  
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
int speedIndex = 0;

int input;

bool debug = true;

bool leftMotorIN1Bool = 0, leftMotorIN2Bool = 0,
     rightMotorIN1Bool = 0, rightMotorIN2Bool = 0;

//ERROR FUNCTION & PID VARIABLES
double k1[4] = {50, 30, 25, 20};
double k2[4] = {50, 30, 25, 20};
double Kp = 20.0, Ki = 0.0, Kd = 0.0;

double kPV[3] = {20000.0, 10000.0, 4000.0};


//IMPORT MODULES
#include "interrupt.h"
#include "pid.h"
#include "dictionary.h"
#include "interpreter.h"
#include "L298N.h"


void setup()
{
  WiFi.mode(WIFI_STA);
  esp_wifi_set_ps (WIFI_PS_NONE);
  /* connecting to WiFi */
  WiFi.config(ip, gw, subnet);
  WiFi.begin(ssid, password);
  btStop();
  /*wait until ESP32 connect to WiFi*/
  while (WiFi.status() != WL_CONNECTED) 
  {
      delay(500);
  }
  /* start Server */
  server.begin();
  //debugServer.begin();
    
	L298NSetup();
	
	interruptSetup();	
}


void loop()
{
    client = server.available(); 
    if (client) 
    {                   
      client.println("Welcome");


      //debugClient = debugServer.available();
      //while(!debugClient)
      //{
      //  debugClient = debugServer.available();
      //}
      //debugClient.println("Welcome");


      /* check client is connected */           
      while (client.connected()) 
      {          
          if (client.available()) 
          {
              input = client.parseInt();
              while (client.available())
              {
                client.read();
              }
              interprete(); 
          }
              if (!debug)
              {
                PID();
              }
    
              L298NMotorDriver();
      }
      debug = true;
      emergencyStop();
      L298NMotorDriver();
    }
}
