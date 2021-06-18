#include "DFRobot_PH.h"
#include "GravityTDS.h"
#include "DFRobot_EC.h"
#include <EEPROM.h>

#define PH_PIN A0
#define TdsSensorPin A1
#define EC_PIN A2

float temperature = 19,tdsValue, phValue, ecValue, voltage = 0;

DFRobot_PH ph;
GravityTDS gravityTds;
DFRobot_EC ec;

void setup()
{
    Serial.begin(115200);  
    ph.begin();
    ec.begin();
    gravityTds.setPin(TdsSensorPin);
    gravityTds.setAref(5.0);  //reference voltage on ADC, default 5.0V on Arduino UNO
    gravityTds.setAdcRange(1024);  //1024 for 10bit ADC;4096 for 12bit ADC
    gravityTds.begin();  //TDS initialization
}

void loop()
{
    static unsigned long timepoint = millis();
    if(millis()-timepoint>1000U){                  //time interval: 1s
        timepoint = millis();
        //temperature = readTemperature();         // read your temperature sensor to execute temperature compensation
        voltage = analogRead(PH_PIN)/1024.0*5000;  // read the voltage
        phValue = ph.readPH(voltage,temperature);  // convert voltage to pH with temperature compensation
        Serial.print("pH:");
        Serial.println(phValue,2);

        //temperature = readTemperature();  //add your temperature sensor and read it
        gravityTds.setTemperature(temperature);  // set the temperature and execute temperature compensation
        gravityTds.update();  //sample and calculate
        tdsValue = gravityTds.getTdsValue();  // then get the value
        Serial.print(tdsValue,0);
        Serial.println("ppm");
        
        //temperature = readTemperature();          // read your temperature sensor to execute temperature compensation
        voltage = analogRead(EC_PIN)/1024.0*5000;   // read the voltage
        ecValue =  ec.readEC(voltage,temperature);  // convert voltage to EC with temperature compensation
        Serial.print("EC: ");
        Serial.print(ecValue);
        Serial.println("ms/cm");
    }
}

float readTemperature()
{
  //add your code here to get the temperature from your temperature sensor
}
