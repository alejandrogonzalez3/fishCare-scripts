#!/usr/bin/env python3

# Notas de autor: 
# 1.- O Relé ten que estar a 3.3v para funcionar.
# 2.- Os pins están en BCM, polo tanto hai que conectar ao GPIO 17, pin 11 (6º comezando dende arriba, fila da esquerda)

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

RELAY_1_GPIO = 17

# The callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))
    # Subscribe to the topic
    client.subscribe("raspberry_relay/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    decodedString = str(msg.payload.decode())
    print("Message received-> " + msg.topic + " " + decodedString)
    if "oxigenator" in msg.topic:
        if "on" in decodedString:
            GPIO.output(RELAY_1_GPIO, GPIO.LOW)
        elif "off" in decodedString:
            GPIO.output(RELAY_1_GPIO, GPIO.HIGH)

try:
    GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
    GPIO.setup(RELAY_1_GPIO, GPIO.OUT, initial = GPIO.HIGH) # GPIO Assign mode

    client = mqtt.Client()
    client.on_connect = on_connect  # Define callback function for successful connection
    client.on_message = on_message  # Define callback function for receipt of a message

    # Connect to (broker, port, keepalive-time)
    client.connect("broker.mqttdashboard.com", 1883, 60)

    client.loop_forever()  # Start networking daemon
    
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("\nKeyboard interrupt")

finally:
   print("clean up GPIO pins") 
   GPIO.cleanup()
