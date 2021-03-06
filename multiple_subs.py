import threading
import time
import psutil
import signal

import random
from client import MQTT

from csv import writer

STOPPED = False

def new_sub(cid = 'sub'):
    mqtt = MQTT()
    client = mqtt.connect_mqtt(cid)

    def on_message(client, userdata, msg):
        pass

    client.subscribe(mqtt.topic)
    client.on_message = on_message
    client.loop_forever()


n = 0
while True:
    with open('subs_data.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        cpu = psutil.cpu_percent(5)
        ram = psutil.virtual_memory()[2]
        print('CPU usage: ', cpu)
        print('RAM usage:', ram)
        csv_writer.writerow([n, cpu, ram])

    n += 1
    print(f"Iniciada thread {n}")
    threading.Thread(target=new_sub, args=(f's{n}', )).start()
