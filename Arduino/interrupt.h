/* INTERRUPT MODULES
*Use interrupt to count number of pulse from encoder
́*
*Created 20190315 by nguyenmthien
*Last edited 20190317
*
*REQUIREMENTS:
*    VARIABLES: 
*       double omegal, omegar
*       bool  leftMotorIN1Bool, leftMotorIN2Bool, 
*            rightMotorIN1Bool, rightMotorIN2Bool: OUTPUT motor driver input pins
*    ETC: 
*       the following should be in void setup():
*           attachInterrupt(digitalPinToInterrupt(2), countLeft, RISING); 
*           attachInterrupt(digitalPinToInterrupt(3), countRight, RISING);
*
*OUTPUTS: countLeft(): leftCount counts number of pulse by left encoder
*         countRight(): rightCount counts number of pulse by right encoder
*
*PINOUT: Left Motor encoder  -> pin 2
*        Right Motor encoder -> pin 3
*/
 

 
void countLeft()
{
    previoust = t;
    t = micros();
    
    if ((leftMotorIN1Bool==0) && (leftMotorIN2Bool==1)) //check if moving forward
    {
        omegal = -0.0174532925199432958/(double(t) - double(previoust));
    }
    if ((leftMotorIN1Bool==1) && (leftMotorIN2Bool==0)) //check if moving backward
    {
        omegal = 0.0174532925199432958/(double(t) - double(previoust));
    }
}

void countRight()
{
    previoust = t;
    t = micros();
    
    if ((rightMotorIN1Bool==0) && (rightMotorIN2Bool==1)) //check if moving forward
    {
        omegar = -0.0174532925199432958/(double(t) - double(previoust));
    }
    if ((rightMotorIN1Bool==1) && (rightMotorIN2Bool==0)) //check if moving backward
    {
        omegar = 0.0174532925199432958/(double(t) - double(previoust));
    }
}

void interruptSetup()
{
    pinMode(2, INPUT);
	pinMode(3, INPUT);
    
    attachInterrupt(digitalPinToInterrupt(2), countLeft, RISING);
    attachInterrupt(digitalPinToInterrupt(3), countRight, RISING);
} 
