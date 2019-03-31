void SocketServer(){ 

  WiFiClient client = wifiServer.available();

  if (client) {
 
    while (client.connected()) {   // while the client is still connected do:
      String strInput = "";        // strInput is a string that will be appended     
      while (client.available()) {      // while there are still datas sent to the client do:
          input = client.read() ;     // read the char type input from client and 
          strInput.concat(input);  // concat: append remaining character from input to strInput String 
      }                     
      int intInput = strInput.toInt();  // convert the strInput String into integer 
      interprete(intInput, client);   // interprete function with two variable intInput and client 
      if (!debug)
      {
        PID();
      }
    
      L298NMotorDriver();
      delay(0.01);
    }
 
//    client.stop();                      // out of the while connected loop do:
//    Serial.println("Client disconnected");  
 
  }
}
