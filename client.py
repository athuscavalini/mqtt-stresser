from paho.mqtt import client as mqtt_client
import random

class MQTT:
    "Cliente MQTT"
    broker = 'localhost'
    port = 1883
    topic = "/python/mqtt"
    client_id = f'python-mqtt-{random.randint(0, 1000)}'

    def connect_mqtt(self, cid = None):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
        # Set Connecting Client ID
        client = mqtt_client.Client(cid or self.client_id)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client