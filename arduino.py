import serial

import requests
import json
import sys

arduino = serial.Serial('/dev/ttyACM0', 115200)

baseUrl = "http://localhost:8080"

authenticateUrl = baseUrl + "/user/login"
sensorUrl = baseUrl + "/sensorValue/store"

username = "alex"
password = "alex"

print("Starting!")

count = 0

while True:
      # Authentication
      # authenticate = requests.post(authenticateUrl, params = {'username':username, 'password':password})
      # print("Token: %s" % authenticate.text)

      if (count == 3):
          sys.exit()


      if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').rstrip()
            print(line[4:])
            value = line[4:]

            if "pH" in line:
                  count += 1
                  # r = requests.post(sensorUrl, params = {'sensorName':'pH', 'value':line}, headers={"content-type":"json", "apiToken":apiToken})
                  r = requests.post(sensorUrl, params = {'sensorName':'pH', 'value': value, 'hatcheryId': '1'})
                  print("pH POST response: %s" % r.status_code)
                  #print("pH Value:", line)
            if "EC" in line:
                  count += 1
                  # r = requests.post(sensorUrl, params = {'sensorName':'conductivity', 'value':line}, headers={"content-type":"json", "apiToken":apiToken})
                  r = requests.post(sensorUrl, params = {'sensorName':'salinity', 'value': value, 'hatcheryId': '1'})
                  print("conductivity POST response: %s" % r.status_code)
                  #print("conductivity Value:", line)
            if "dO" in line:
                  count += 1
                  # r = requests.post(sensorUrl, params = {'sensorName':'conductivity', 'value':line}, headers={"content-type":"json", "apiToken":apiToken})
                  r = requests.post(sensorUrl, params = {'sensorName':'do', 'value': value, 'hatcheryId': '1'})
                  print("dO POST response: %s" % r.status_code)
                  #print("DO value:", line)


arduino.close() #Finalizamos la comunicacion
