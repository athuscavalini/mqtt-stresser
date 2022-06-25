from client import MQTT
import time

mqtt = MQTT()

client = mqtt.connect_mqtt()
client.loop_start()

msg = '0' * 100000
while True:
    result = client.publish(mqtt.topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Published. Size {len(msg)}")
    else:
        print(f"Failed to publish message of size {len(msg)}")
        break
    msg += '0' * 100000
    time.sleep(0.1)