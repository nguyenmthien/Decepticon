void WifiSetup(){
  Serial1.begin(115200);   // communication with the host computer 
  WiFi.config(ip, gw, subnet);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
//  Serial1.print("\nConnecting to "); Serial1.println(ssid);
  uint8_t i = 0;
  while (WiFi.status() != WL_CONNECTED && i++ < 20) delay(500);
  if(i == 21){
//    Serial1.print("Could not connect to"); Serial1.println(ssid);
    while(1) delay(0.01);
  }
  //start UART and the server
//  Serial.begin(115200);     // just adjust baudrate from 115200 to 9600
  wifiServer.begin();
  wifiServer.setNoDelay(true);
}
