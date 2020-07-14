import threading


class MyThread(threading.Thread):

    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        print("Value send", self.h)


thread_a = MyThread(1)
thread_a.start()
