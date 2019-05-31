/* PID function
*Controller use the postions of instantaneous centers of rotation as terms for error function
*
*Created 20190317 by nguyenmthien
*Last edited 20190326
*
*REQUIREMENTS:
*    VARIABLES:
*        unsigned long tau, previoustau, dtau: time terms
*        int theta: input angle of movement
*        double Kp, Ki, Kd: error function and PID variables
*		 array k1, k2			 
*        double PVl, PVr, SPl, SPr, El, Er, Ul, Ur: PID functions
*        double previousEl, previousEr, previousI: PID reset variables
*        long leftCount, rightCount:  pulse count by encoder, ouput of interrupt.h
*        long previousLeftCount, previousRightCount: reset variables of leftCount and rightCount
*
*OUTPUTS:
*    Ul: control variable for left motor
*    Ur: control variable for right motor
*/   
    
        
void PID()
{
    //calculate dtau:
    tau = micros();
    dtau = (tau - previoustau);
    
    
    //Processed values:
    PVl = omegal * kPV[speedIndex];
    PVr = omegar * kPV[speedIndex];

    if ((PVl < 1.0) && (PVl > -1.0))
    {
      PVl = 0; 
    }
    if ((PVr < 1.0) && (PVl > -1.0))
    {
      PVr = 0;
    }

    //Set points:
	if ( theta != 999 )
	{
		SPl = k1[speedCount]*cos(theta) - k2[speedCount]*sin(theta);     // k1   k2
		SPr = k1[speedCount]*cos(theta) + k2[speedCount]*sin(theta);     // k1   k2
    }
	else 
	{
		SPl = 0;
		SPr = 0;	
    }

    
    //Error function:
    El = SPl - PVl;
    Er = SPr - PVr;

    
    //debugClient.print(Ul); debugClient.print(" "); debugClient.println(Ur);
    
    
    //PID formulas:
    Ul = (Kp * El)  +  Ki * (previousIl + El * dtau) + (Kd * (El - previousEl) / dtau);
    Ur = (Kp * Er)  +  Ki * (previousIr + Er * dtau) + (Kd * (Er - previousEr) / dtau);


    
    //Reset time and values for derivative limit and Riemann sum:
    previousEl = El;
    previousEr = Er;
    previousIl = previousIl + El * dtau;
    previousIr = previousIr + Er * dtau;
    previoustau = micros();
}
   
