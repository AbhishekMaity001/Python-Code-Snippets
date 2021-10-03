import time
import threading # importing the threading module (older way)
start = time.perf_counter()

# Any Function which is consuming some amount of time
def do_something(seconds) :
    print(f'Sleeping {seconds} seconds....thread ')
    time.sleep(seconds)
    print('Done Sleeping...thread ')

# Now callling the functions directly (naive method)
# do_something(1)
# do_something(1)

# t1 = threading.Thread(target=do_something, args=[1])
# t2 = threading.Thread(target=do_something, args=[1])
# t1.start()
# t2.start()
# t1.join() # .join will just make sure that after all your threads are executed then halt the main program and after
# t2.join() # execution of all the threads then resume the rest of the program. ie... count the total time taken after all your threads are completed fully

threadslist = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[2]) # This is a generic line of code to create a thread. Now loop on this 
    t.start()
    threadslist.append(t) # keep on appending to a list as the threads are starting one by one 

# Now loop through that threads list and join all those so that the program will end once all the processes are done executing!
for thread in threadslist: 
    thread.join()

finish= time.perf_counter()
print(f'finished in {round(finish-start,2)} seconds')