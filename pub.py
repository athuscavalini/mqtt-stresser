from client import MQTT
import time

mqtt = MQTT()

def run():
    client = mqtt.connect_mqtt()
    client.loop_start()
    msg = 'Message!'
    result = client.publish(mqtt.topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{mqtt.topic}`")
    else:
        print(f"Failed to send message to topic {mqtt.topic}")

if __name__ == '__main__':
    run()