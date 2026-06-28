#multithreading=used to perform multiple tasks concurrently(at the same time)
#             allows you to execute multiple tasks at the same time,good at I/O tasks like reading files or fetching data from API'S
#            threading.Thread(target=function_name)


import threading
import time

def walk_dog(first):
    time.sleep(7)
    print(f"walking {first}")

def take_out_trash():
    time.sleep(5)
    print("taking out the trash")

def get_mail():
    time.sleep(3)
    print("getting mail")

chore1 = threading.Thread(target=walk_dog,args=["Scooby"])
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("all chores completed")