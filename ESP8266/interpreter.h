/* INTERPRETER MODULE
*interprete input to commands

*REQUIREMENT
*	VARIABLES
*		string input
*		int inputINT
*		bool debug
 */
 
void interprete(int input, WiFiClient client) 
{
 
    switch (input)
	{
		case 998:
		{
			emergencyStop();
			debug = true;
//      client.println(Ul);
//      client.println(Ur);
			client.println("emergencyStop");
//      client.println(leftMotorPWM);
//      client.println(leftMotorIN1);
      resetPID();
			break;
		}
		case 994:
		{
			bothUp();
			debug = true;
//      client.println(Ul);
//      client.println(Ur);
			client.println("bothUp");
      resetPID();
			break;
		}
		case 993:
		{
			bothDown();
			debug = true;
			client.println("bothDown");
      resetPID();
			break;
		}
		case 992:
		{
			leftUpRightDown();
			debug = true;
			client.println("leftUpRightDown");
      resetPID();
			break;
		}
		case 991:
		{
			leftDownRightUp();
			debug = true;
			client.println("leftDownRightUp");
      resetPID();
			break;
		}
		case 990:
		{
			speedUp();
			debug = false;
			client.println("speedUp");
      resetPID();
			break;
		}
		case 988:
		{
			speedDown();
			debug = false;
			client.println("speedDown");
      resetPID();
			break;
		}
   case 999:
   {
      theta = 999;
      debug = false;
      break;
   }
		default: 
   {
      if ((input < 360) && (input > -360))
      {   
			  theta = input * 0.0174532925199432958; // to radians
			  debug = true;
			  break;
      }
   }
	}
	
}
