/**
 Basic demonstration of using a joystick.
 
 When this sketch runs it will try and find
 a game device that matches the configuration
 file 'joystick' if it can't match this device
 then it will present you with a list of devices
 you might try and use.
 
 The chosen device requires 2 sliders and 2 buttons.
 */
import java.awt.Robot;
import java.awt.event.KeyEvent;
import java.io.IOException;
 
import org.gamecontrolplus.gui.*;
import org.gamecontrolplus.*;
import net.java.games.input.*;

ControlIO control;
ControlDevice stick;

double px, py, tan, phi,intPhi;
int i;
String outputPhi;
public void setup() 
{
  size(100, 100);
  // Initialise the ControlIO
  control = ControlIO.getInstance(this);
  // Find a device that matches the configuration file
  stick = control.getMatchedDevice("joystick");
}

public void getUserInput() 
{  
  px = map(stick.getSlider("X").getValue(), -1, 1, 0, width);
  py = map(stick.getSlider("Y").getValue(), -1, 1, 0, height);
  tan=(px-50)/(py-50);
    phi=Math.atan((px-50)/(py-50));
    println(phi);
}




public void draw() {
  getUserInput();
  try {
    Robot r=new Robot();  

if (( px>=51 || px<=49) && (py>=51|| py<=49)) 
{
  i= (int) phi;
     outputPhi = String.format("%02d",intPhi);
    char c;
     int d=outputPhi.length(),e=0,f=0;
      
     while(e<=d)
    {
     c=outputPhi.charAt(e);
     f=(int) c; //converts character to Unicode. 
     r.keyPress(KeyEvent.getExtendedKeyCodeForChar(f));
     e++;
      Thread.sleep(100);
      if (e==d)
      {r.keyPress(KeyEvent.VK_ENTER);
      r.keyRelease(KeyEvent.VK_ENTER);
      }
    }
    }
  }

  
  
  catch (Exception e) 
  {
    //Uh-oh...
    e.printStackTrace();
  }
  
  }
