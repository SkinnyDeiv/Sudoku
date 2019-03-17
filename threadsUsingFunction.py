import threading

def threadFunction(intA, intB):
    intResult = intA + intB
    print(intResult)

threadA = threading.Thread(target=threadFunction, args=(22, 21))
threadA.start()
