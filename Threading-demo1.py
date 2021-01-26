import time
import threading
start = time.perf_counter()


def do_something(seconds) :
    print(f'Sleeping {seconds} seconds....thread ')
    time.sleep(1)
    print('Done Sleeping...thread ')

# do_something()
# do_something()

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
# t1.start()
# t2.start()
# t1.join() # .join will just make sure that after all ure threads are executed then halt the main program and after
# t2.join() # execution of all the threads then resume the rest of the program

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish= time.perf_counter()
print(f'finished in {round(finish-start,2)} seconds')