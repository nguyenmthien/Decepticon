/*MAIN PROGRAM
Created 20190319
Last edited 20190320
*/


//DEFINE PINS
int leftMotorIN1 = 13, leftMotorIN2 = 12,
    rightMotorIN1 = 10, rightMotorIN2 = 8,
    leftMotorPWM = 11, rightMotorPWM = 9 ;

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


void setup()
{
	L298NSetup();
	
	interruptSetup();
	
	arduinoESPSetup();
}


void loop()
{
    if (Serial.available()>1)
	{
		input = Serial.parseInt();
		interprete();
	}
    
	if (!debug)
	{
		PID();
	}
    
	L298NMotorDriver();
}
