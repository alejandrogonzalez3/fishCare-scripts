#!/usr/bin/python3
import time
from w1thermsensor import W1ThermSensor

import requests
import json
import sys

sensor = W1ThermSensor()

baseUrl = "http://localhost:8080"

authenticateUrl = baseUrl + "/user/login"
temperatureUrl = baseUrl + "/sensorValue/store"

username = "alex"
password = "alex"

while True:
    try:
        # Sensor value
        temperature = sensor.get_temperature()

        # For testing
        #temperature = 14.58

        print("Temperatura: %s centigrados" % temperature)

        # authenticate = requests.post(authenticateUrl, params = {'username':username, 'password':password})
        # print("Token: %s" % authenticate.text)
        #r = requests.post(temperatureUrl, data = {'value':temperature}, headers={"content-type":"json", "apiToken":apiToken})
        r = requests.post(temperatureUrl, params = {'sensorName':'temperature', 'value':temperature, 'hatcheryId': '1'})
        print("Temperature POST response: %s" % r.status_code)
        if (r.status_code == 200):
            sys.exit()
        time.sleep(1)
    except requests.exceptions.HTTPError as e:
        time.sleep(10)

