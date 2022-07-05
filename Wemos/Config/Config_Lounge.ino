/*
    DS18B20 Basic Code
    Temperatur auslesen mit einem DS18B20 Temperaturfühlers
    Created by Thomas Zaußnig, 2022
*/

#include <OneWire.h>
#include <DallasTemperature.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

// Der PIN D2 (GPIO 4) wird als BUS-Pin verwendet
#define ONE_WIRE_BUS 4
#define USE_SERIAL Serial

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature DS18B20(&oneWire);
WiFiClient wifiClient;

// In dieser Variable wird die Temperatur gespeichert
float temperature;
const char* ssid = "A1-2453B3";
const char* password = "QAYPLNA6P6";

void setup() {
  USE_SERIAL.begin(115200);

  // DS18B20 initialisieren
  DS18B20.begin();
  
  USE_SERIAL.print("Connecting to ");
  USE_SERIAL.println(ssid);
  WiFi.hostname("Name");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    USE_SERIAL.print(".");
  }
  USE_SERIAL.println("");
  USE_SERIAL.println("WiFi connected");

  USE_SERIAL.print("IP Adress: ");
  USE_SERIAL.println(WiFi.localIP());
  USE_SERIAL.print("MAC Address: ");
  USE_SERIAL.println(WiFi.macAddress());
}

void loop() {
  DS18B20.requestTemperatures();
  temperature = DS18B20.getTempCByIndex(0);

  char
  // Ausgabe im seriellen Monitor
  USE_SERIAL.println(String(temperature) + " °C");
  
  String url = "http://10.0.0.6/test.php?ipsrc=Lounge&temperature="+ String(temperature) + "&humidity=1&voltage=1";
  USE_SERIAL.println(url);
  HTTPClient http;

  http.begin(wifiClient, url); //HTTP
  USE_SERIAL.print("[HTTP] GET...\n");
  // start connection and send HTTP header
  int httpCode = http.GET();
 
    // httpCode will be negative on error
    if(httpCode > 0) {
        // HTTP header has been send and Server response header has been handled
        USE_SERIAL.printf("[HTTP] GET... code: %d\n", httpCode);
 
        // file found at server
        if(httpCode == HTTP_CODE_OK) {
            String payload = http.getString();
            USE_SERIAL.println(payload);
        }
    } else {
        USE_SERIAL.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
    }
 
    http.end();
    delay(300000);   // wait a minute
    
}
