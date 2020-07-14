import threading
import time
import datetime

time_a = datetime.datetime.now()
list_a = []


def joinFunction(entry):
    time.sleep(1)
    list_a.append(entry)


list_thread = []
for each in range(10):
    thread_a = threading.Thread(target=joinFunction, args=(each,))
    list_thread.append(thread_a)
    thread_a.start()

for thread in list_thread:
    thread.join()

print("List is:", list_a)
timeB = datetime.datetime.now()
print("Time taken", timeB - time_a)
