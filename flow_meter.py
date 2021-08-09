#!/usr/bin/env python3

# https://www.raspberrypi.org/forums/viewtopic.php?t=118230

# Connection schema:
# Red ------------- 5V
#
#            +----- 3V3
#            |
#           10K
#            |
# Yellow ----+----- gpio
#
# Black ----------- Ground

import RPi.GPIO as GPIO
import time, sys

baseUrl = "http://localhost:8080"

authenticateUrl = baseUrl + "/user/login"
temperatureUrl = baseUrl + "/sensorValue/store"

username = "string"
password = "string"

FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
   global count
   count += 1
   flow = count / (60 * 7.5)
   # print(f'The flow is: {flow:.2f}')
   print("Have flow")
   
   # authenticate = requests.post(authenticateUrl, params = {'username':username, 'password':password})
   # print("Token: %s" % authenticate.text)
   # r = requests.post(temperatureUrl, data = {'value':temperature}, headers={"content-type":"json", "apiToken":apiToken})
   #r = requests.post(temperatureUrl, params = {'sensorName':'temperatura', 'value':temperature})
   #print("Temperature POST response: %s" % r.status_code)
   GPIO.cleanup()
   sys.exit()

GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

while True:
    try:
        time.sleep(10)
        print("Haven't flow")
        # authenticate = requests.post(authenticateUrl, params = {'username':username, 'password':password})
        # print("Token: %s" % authenticate.text)
        # r = requests.post(temperatureUrl, data = {'value':temperature}, headers={"content-type":"json", "apiToken":apiToken})
        #r = requests.post(temperatureUrl, params = {'sensorName':'temperatura', 'value':temperature})
        #print("Temperature POST response: %s" % r.status_code)
        GPIO.cleanup()
        sys.exit()

    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        print("\nKeyboard interrupt")
        GPIO.cleanup()
        sys.exit()

