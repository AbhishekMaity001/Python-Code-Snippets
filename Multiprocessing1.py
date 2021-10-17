
# This is the older way of doing the multiprocessing using .start() & .join() methods!
# This is the older way of doing the multiprocessing using .start() & .join() methods!
import time
import multiprocessing

t1 = time.perf_counter()

def do_something():
    print('Starting to Sleep 1 second')
    time.sleep(2)
    print('Done Sleeping....')
    return 1, 2


if __name__ == '__main__':
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    t2 = time.perf_counter()
    print(f"Total seconds taken : {round(t2 - t1, 2)} second(s)")

