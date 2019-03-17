import threading
import time
import datetime

timeA = datetime.datetime.now()
listA = []

def joinFunction(entry):
    time.sleep(1)
    listA.append(entry)

listThread = []
for each in range(10):
    threadA = threading.Thread(target=joinFunction, args=(each, ))
    listThread.append(threadA)
    threadA.start()
    threadA.join()

print("List is:", listA)
timeB = datetime.datetime.now()
print("Time taken", timeB - timeA)