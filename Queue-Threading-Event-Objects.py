import time, queue, threading
import queue
import numpy as np

'''Threading events: So When we need to communicate threads with each other then we need Event Objects
   It basically works as a switch , so when one thread does something then the other thread reacts to it.
   Its similar to queue that another thread puts something in the queue and when the queue is empty then that thread will be waiting still.
   It is set to True with the set()
   It is set to False with the clear()
'''

# event = threading.Event()
# event.set() # giving green signal
# event.clear() # giving red signal

# event.wait() # it will wait untill event.set() is true in other words if event.clear() is called then event.wait() will start blocking!!!

# event.is_set()

def flag():
    time.sleep(5)
    event.set()
    print('starting count down!!')
    time.sleep(5)
    print("Event is cleared (done sleeping 5 seconds)")
    event.clear() # once event.clear is called then it will send a indication of blocking

def start_operations():
    event.wait()
    while event.is_set():
        x = np.random.randint(30)
        print('Start random no.s throw', x)
        time.sleep(1)
        if x == 29:
            print('True')
    print('Event has been cleared now event.clear() is called !!')

event = threading.Event()
print('starting thread execution')
t1 = threading.Thread(target=flag)
t2 = threading.Thread(target=start_operations)
t1.start()
t2.start()



