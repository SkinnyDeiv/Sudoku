import threading
import time

def threadFunction(intA, intB):
    time.sleep(1)
    intResult = intA + intB
    print(intResult)

threadA = threading.Thread(target=threadFunction, args=(10, 11))
threadA.start()

threadB = threading.Thread(target=threadFunction, args=(21, 22))
threadB.start()

print("Total number of threads:", threading.active_count())
print("List of threads:\n", threading.enumerate())