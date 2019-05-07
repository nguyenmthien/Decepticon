/* MODULES FOR DICTIONARY
implement of the dictionary

REQUIREMENT
	VARIABLES
		byte speedCount: count variable in k1 and k2 arrays
 */

void resetPID()
{
    theta = 999;
    previousEl = 0;
    previousEr = 0;
    previousIl = 0;
    previousIr = 0;
} 
 
void emergencyStop()
{
    Ul = 0;
    Ur = 0;
}

void bothUp()
{
    Ul = 255;
    Ur = 255;
}

void bothDown()
{
    Ul = -255;
    Ur = -255;
}

void leftUpRightDown()
{
    Ul = 255;
    Ur = -255;
}

void leftDownRightUp()
{
    Ul = -255;
    Ur = 255;
}

void speedUp()
{
    if (speedCount < 2)
	{
		speedCount++;
	}
}

void speedDown()
{
	if (speedCount > 0)
	{
		speedCount--;
	}
}

void increaseSpeed()
{
    if (speedIndex < 2)
    {
        speedIndex++;
    }
}

void decreaseSpeed()
{
    if (speedIndex > 0)
    {
        speedIndex--;
    }
}
