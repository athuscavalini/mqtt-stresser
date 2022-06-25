import frequency
import threading
import time
import psutil

from csv import writer

n = 1
while True:
    print(f"Iniciada thread {n}")
    threading.Thread(target=frequency.run, args=(str(n),True,'1')).start()
    n += 1
    time.sleep(5)

    with open('pubs_data.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        cpu = psutil.cpu_percent(5)
        ram = psutil.virtual_memory()[2]
        print('CPU usage: ', cpu)
        print('RAM usage:', ram)
        csv_writer.writerow([n, cpu, ram])