import serial

import requests
import json

arduino = serial.Serial('/dev/ttyACM0', 115200)

baseUrl = "http://localhost:8080"

authenticateUrl = baseUrl + "/user/login"
temperatureUrl = baseUrl + "/sensorValue/store"

username = "string"
password = "string"

print("Starting!")

while True:
      # Authentication
      # authenticate = requests.post(authenticateUrl, params = {'username':username, 'password':password})
      # print("Token: %s" % authenticate.text)
            
      if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').rstrip()
            # print(line)
            if "ppm" in line:
                  # r = requests.post(temperatureUrl, data = {'value':tds}, headers={"content-type":"json", "apiToken":apiToken})
                  # r = requests.post(temperatureUrl, params = {'sensorName':'tds', 'value':line})
                  # print("TDS POST response: %s" % r.status_code)
                  print("TDS Value:", line)
            if "pH" in line:
                  # r = requests.post(temperatureUrl, data = {'value':pH}, headers={"content-type":"json", "apiToken":apiToken})
                  # r = requests.post(temperatureUrl, params = {'sensorName':'pH', 'value':line})
                  # print("pH POST response: %s" % r.status_code)
                  print("pH Value:", line)

arduino.close() #Finalizamos la comunicacion
