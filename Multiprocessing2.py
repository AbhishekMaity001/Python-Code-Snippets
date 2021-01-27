import time
import concurrent.futures

t1 = time.perf_counter()

def do_something():
    print("Sleeping for 1 seconds..")
    time.sleep(1)
    print("Done Sleeping...!!")



if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # result = executor.submit(do_something())
        results = [executor.submit(do_something)  for _ in range(10)]

    t2 = time.perf_counter()
    print(f"Total seconds taken : {round(t2 - t1, 2)} second(s)")
