import paho.mqtt.client as paho
import sys

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Couldnt connect to MQTT")
    sys.exit(-1)

client.publish("Temp", "30", 0)

client.disconnect()

