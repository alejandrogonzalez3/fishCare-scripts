import serial

import requests
import json

arduino = serial.Serial('/dev/ttyACM0', 115200)

baseUrl = "http://localhost:8080"

authenticateUrl = baseUrl + "/user/login"
sensorUrl = baseUrl + "/sensorValue/store"

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
                  # r = requests.post(sensorUrl, params = {'sensorName':'tds', 'value':line}, headers={"content-type":"json", "apiToken":apiToken})
                  # r = requests.post(sensorUrl, params = {'sensorName':'tds', 'value':line})
                  # print("TDS POST response: %s" % r.status_code)
                  print("TDS Value:", line)
            if "pH" in line:
                  # r = requests.post(sensorUrl, params = {'sensorName':'pH', 'value':line}, headers={"content-type":"json", "apiToken":apiToken})
                  # r = requests.post(sensorUrl, params = {'sensorName':'pH', 'value':line})
                  # print("pH POST response: %s" % r.status_code)
                  print("pH Value:", line)
            if "ms/cm" in line:
                  # r = requests.post(sensorUrl, params = {'sensorName':'conductivity', 'value':line}, headers={"content-type":"json", "apiToken":apiToken})
                  # r = requests.post(sensorUrl, params = {'sensorName':'conductivity', 'value':line})
                  # print("conductivity POST response: %s" % r.status_code)
                  print("conductivity Value:", line)

arduino.close() #Finalizamos la comunicacion
