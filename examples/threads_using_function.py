import threading


def thread_function(int_a, int_b):
    int_result = int_a + int_b
    print(int_result)


thread_a = threading.Thread(target=thread_function, args=(22, 21))
thread_a.start()
