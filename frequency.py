from client import MQTT
import time

def run(cid = None, silence = False, msg = '0'):
    mqtt = MQTT()

    client = mqtt.connect_mqtt(cid)
    client.loop_start()

    msg = msg * 100
    msg_number = 1
    while True:
        result = client.publish(mqtt.topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            if not silence: print(f"Published message {msg_number}")
        else:
            print(f"Failed to publish message{msg_number}")
            break
        msg_number += 1
        time.sleep(0.1)

if __name__ == '__main__':
    run()