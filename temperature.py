#!/usr/bin/python3
import time
from w1thermsensor import W1ThermSensor

import requests

sensor = W1ThermSensor()

authenticateUrl = ""
temperatureUrl = ""

while True:
    try:
        temperature = sensor.get_temperature()
        print("Temperatura: %s centigrados" % temperature)
        # Meter Token de autenticacion
        # authenticate = requests.post(authenticateUrl, data = {'username':username, 'password':password})
        # r = requests.post(temperatureUrl, data = {'value':temperature}, headers={"content-type":"json", "apiToken":apiToken})
        
        # r = requests.post(temperatureUrl, data = {'value':temperature})
        time.sleep(1)
    except requests.exceptions.HTTPError as e:
        time.sleep(10)
    
