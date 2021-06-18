#!/usr/bin/env python3
import paho.mqtt.client as mqtt

# The callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    # Print result of connection attempt
    print("Connected with result code {0}".format(str(rc)))
    # Subscribe to the topic
    client.subscribe("raspberry_relay/oxigenator")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Message received-> " + msg.topic + " " + str(msg.payload.decode()))

client = mqtt.Client()  # Create instance of client with client ID “digi_mqtt_test”
client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message

# Connect to (broker, port, keepalive-time)
client.connect("broker.mqttdashboard.com", 1883, 60)

client.loop_forever()  # Start networking daemon
