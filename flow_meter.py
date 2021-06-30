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

FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
   global count
   count += 1
   flow = count / (60 * 7.5)
   print(f'The flow is: {flow:.2f}')

GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

while True:
    try:
        time.sleep(1)

    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        print("\nKeyboard interrupt")
        GPIO.cleanup()
        sys.exit()
        
