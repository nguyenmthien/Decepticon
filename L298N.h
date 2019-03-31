/* 
Pins for Motor 1 Left
#define leftMotorIN1 13 //IN1 
#define leftMotorIN2 15 //IN2 
#define leftMotorPWM 14 //ENA 

Pins for Motor 2 Right
#define rightMotorIN1 3 //IN3 
#define rightMotorIN2  1 //IN4 
#define rightMotorPWM 12 //ENB 
 */
void L298NSetup()
{
   pinMode(leftMotorIN1, OUTPUT);
   pinMode(leftMotorIN2, OUTPUT);
   pinMode(rightMotorIN1, OUTPUT);
   pinMode(rightMotorIN2, OUTPUT);
   pinMode(leftMotorPWM, OUTPUT);
   pinMode(rightMotorPWM, OUTPUT);
   
   
   digitalWrite(leftMotorIN1, LOW);
   digitalWrite(leftMotorIN2, LOW);
   digitalWrite(rightMotorIN1, LOW);
   digitalWrite(rightMotorIN2, LOW);
   analogWrite(leftMotorPWM, 0);
   analogWrite(rightMotorPWM, 0);
}  

void L298NMotorDriver()
{
    if (Ul < 0)
    {
        leftMotorIN1Bool = 0;
        leftMotorIN2Bool = 1;
        digitalWrite(leftMotorIN1, leftMotorIN1Bool);
        digitalWrite(leftMotorIN2, leftMotorIN2Bool);
        analogWrite(leftMotorPWM, -Ul);
    }
    
    if (Ul > 0)
    {
        leftMotorIN1Bool = 1;
        leftMotorIN2Bool = 0;
        digitalWrite(leftMotorIN1, leftMotorIN1Bool);
        digitalWrite(leftMotorIN2, leftMotorIN2Bool);
        analogWrite(leftMotorPWM, Ul);
    }
    
    if (Ul == 0)
    {
        leftMotorIN1Bool = 0;
        leftMotorIN2Bool = 0;
        digitalWrite(leftMotorIN1, leftMotorIN1Bool);
        digitalWrite(leftMotorIN2, leftMotorIN2Bool);
        analogWrite(leftMotorPWM, 0);
    }
    
    if (Ur < 0)
    {
        rightMotorIN1Bool = 0;
        rightMotorIN2Bool = 1;
        digitalWrite(rightMotorIN1, rightMotorIN1Bool);
        digitalWrite(rightMotorIN2, rightMotorIN2Bool);
        analogWrite(rightMotorPWM, -Ur);
    }
    
    if (Ur > 0)
    {
        rightMotorIN1Bool = 1;
        rightMotorIN2Bool = 0;
        digitalWrite(rightMotorIN1, rightMotorIN1Bool);
        digitalWrite(rightMotorIN2, rightMotorIN2Bool);
        analogWrite(rightMotorPWM, Ur);
    }
    
    if (Ur == 0)
    {
        rightMotorIN1Bool = 0;
        rightMotorIN2Bool = 0;
        digitalWrite(rightMotorIN1, rightMotorIN1Bool);
        digitalWrite(rightMotorIN2, rightMotorIN2Bool);
        analogWrite(rightMotorPWM, 0);
    }
}
