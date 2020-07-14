import threading
import time


def timeThread(entry):
    time.sleep(3)


threadA = threading.Thread(target=timeThread, args=(1,))
threadA.start()
threadA.join(2)

print(threadA.is_alive())
