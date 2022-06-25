from paho.mqtt import client as mqtt_client
import random
from client import MQTT

mqtt = MQTT()

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        if msg.payload.decode().startswith('1'):
            return
        print(f"Received message of size `{len(msg.payload.decode())}` from `{msg.topic}` topic")

    client.subscribe(mqtt.topic)
    client.on_message = on_message

def run():
    client = mqtt.connect_mqtt('sub')
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()