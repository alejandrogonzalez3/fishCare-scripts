#include "DFRobot_PH.h"
#include "GravityTDS.h"
#include "DFRobot_EC.h"
#include <EEPROM.h>
#include "do_grav.h"

#define PH_PIN A1
#define doPin A0
#define EC_PIN A2

float temperature = 19,tdsValue, phValue, ecValue, voltage = 0;

DFRobot_PH ph;
DFRobot_EC ec;
Gravity_DO DO = Gravity_DO(doPin);

void setup()
{
    Serial.begin(115200);  
    ph.begin();
    ec.begin();
    DO.begin();
}

void loop()
{
    //temperature = readTemperature();         // read your temperature sensor to execute temperature compensation
    voltage = analogRead(PH_PIN)/1024.0*5000;  // read the voltage
    phValue = ph.readPH(voltage,temperature);  // convert voltage to pH with temperature compensation
    Serial.print("pH: ");
    if (isnan(phValue)) {
      Serial.println(0);
    }
    else {
      Serial.println(phValue,2);
    }
    
    //temperature = readTemperature();          // read your temperature sensor to execute temperature compensation
    voltage = analogRead(EC_PIN)/1024.0*5000;   // read the voltage
    ecValue =  ec.readEC(voltage,temperature);  // convert voltage to EC with temperature compensation
    Serial.print("EC: ");
    Serial.println(ecValue);

    Serial.print("dO: ");
    Serial.println(DO.read_do_percentage());

    Serial.flush();

    delay(10000);
}

float readTemperature()
{
  //add your code here to get the temperature from your temperature sensor
}
