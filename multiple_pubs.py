import frequency
import threading
import time
import psutil

n = 1
while True:
    print(f"Iniciada thread {n}")
    threading.Thread(target=frequency.run, args=(str(n),True,)).start()
    n += 1
    time.sleep(5)
    print('CPU usage: ', psutil.cpu_percent(5))
    print('RAM usage:', psutil.virtual_memory()[2])