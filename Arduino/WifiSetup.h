void WifiSetup(){
//  // esp ip 
//  IPAddress ip(192, 168, 137, 128); 
//  IPAddress subnet(255, 255, 255, 0);
//  IPAddress gw(192, 168, 1, 1);
  esp_wifi_set_ps (WIFI_PS_NONE);
  Serial1.begin(115200);   // communication with the host computer 
  WiFi.config(ip, gw, subnet);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  WiFi.setSleep(false);// this code solves my problem

//  Serial1.print("\nConnecting to "); Serial1.println(ssid);
  uint8_t i = 0;
  while (WiFi.status() == WL_CONNECTED && i++ < 20) delay(500);
  if(i == 21){
//    Serial1.print("Could not connect to"); Serial1.println(ssid);
    while(1) delay(0.01);
  }
  //start UART and the server
//  Serial.begin(115200);     // just adjust baudrate from 115200 to 9600
  wifiServer.begin();
  wifiServer.setNoDelay(true);
}
