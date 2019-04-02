/* 
Pins for Motor 1 Left
#define leftMotorIN1 15 //IN1 
#define leftMotorIN2 2 //IN2 
#define leftPWMPin 4 //ENA 

Pins for Motor 2 Right
#define rightMotorIN1 16 //IN3 
#define rightMotorIN2  17 //IN4 
#define rightPWMPin 5 //ENB 
 */

const int freq = 5000;
const int leftPWMPinChannel = 0;
const int rightPWMPinChannel = 1;
const int resolution = 8;
 
void L298NSetup()
{
   pinMode(leftMotorIN1, OUTPUT);
   pinMode(leftMotorIN2, OUTPUT);
   pinMode(rightMotorIN1, OUTPUT);
   pinMode(rightMotorIN2, OUTPUT);
   
   ledcSetup(leftPWMPinChannel, freq, resolution);
   ledcSetup(rightPWMPinChannel, freq, resolution);
   
   ledcAttachPin(leftMotorPWM, leftPWMPinChannel);
   ledcAttachPin(rightMotorPWM, rightPWMPinChannel);

   digitalWrite(leftMotorIN1, LOW);
   digitalWrite(leftMotorIN2, LOW);
   digitalWrite(rightMotorIN1, LOW);
   digitalWrite(rightMotorIN2, LOW);
   ledcWrite(leftPWMPinChannel, 0);
   ledcWrite(rightPWMPinChannel, 0);
}  

void L298NMotorDriver()
{
    if (Ul < 0)
    {
        leftMotorIN1Bool = 0;
        leftMotorIN2Bool = 1;
        digitalWrite(leftMotorIN1, leftMotorIN1Bool);
        digitalWrite(leftMotorIN2, leftMotorIN2Bool);
        ledcWrite(leftPWMPinChannel, -Ul);
    }
    
    if (Ul > 0)
    {
        leftMotorIN1Bool = 1;
        leftMotorIN2Bool = 0;
        digitalWrite(leftMotorIN1, leftMotorIN1Bool);
        digitalWrite(leftMotorIN2, leftMotorIN2Bool);
        ledcWrite(leftPWMPinChannel, Ul);
    }
    
    if (Ul == 0)
    {
        leftMotorIN1Bool = 0;
        leftMotorIN2Bool = 0;
        digitalWrite(leftMotorIN1, leftMotorIN1Bool);
        digitalWrite(leftMotorIN2, leftMotorIN2Bool);
        ledcWrite(leftPWMPinChannel, 0);
    }
    
    if (Ur < 0)
    {
        rightMotorIN1Bool = 0;
        rightMotorIN2Bool = 1;
        digitalWrite(rightMotorIN1, rightMotorIN1Bool);
        digitalWrite(rightMotorIN2, rightMotorIN2Bool);
        ledcWrite(rightPWMPinChannel, -Ur);
    }
    
    if (Ur > 0)
    {
        rightMotorIN1Bool = 1;
        rightMotorIN2Bool = 0;
        digitalWrite(rightMotorIN1, rightMotorIN1Bool);
        digitalWrite(rightMotorIN2, rightMotorIN2Bool);
        ledcWrite(rightPWMPinChannel, Ur);
    }
    
    if (Ur == 0)
    {
        rightMotorIN1Bool = 0;
        rightMotorIN2Bool = 0;
        digitalWrite(rightMotorIN1, rightMotorIN1Bool);
        digitalWrite(rightMotorIN2, rightMotorIN2Bool);
        ledcWrite(rightPWMPinChannel, 0);
    }
}
