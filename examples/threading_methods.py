import threading
import time


def thread_function(int_a, int_b):
    time.sleep(1)
    int_result = int_a + int_b
    print(int_result)


thread_a = threading.Thread(target=thread_function, args=(10, 11))
thread_a.start()

thread_b = threading.Thread(target=thread_function, args=(21, 22))
thread_b.start()

print("Total number of threads:", threading.active_count())
print("List of threads:\n", threading.enumerate())
