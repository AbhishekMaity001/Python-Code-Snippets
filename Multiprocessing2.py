import time
import concurrent.futures

t1 = time.perf_counter()

def do_something(a, b, c=10):
    print("Sleeping for 1 seconds..")
    time.sleep(2)
    # print("Done Sleeping...!!")
    print(str(a)+b)
    return a, b, c



if __name__ == '__main__':

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # result = executor.submit(do_something())
        results = [executor.submit(do_something, i, str(i)+'--abhishek')  for i in range(5)]

    for f in concurrent.futures.as_completed(results): # as_completed will give you a generator object and yield the values of threads as they are completed!
        print(f.result())
        print(type(f.result()))

    t2 = time.perf_counter()
    print(f"Total seconds taken : {round(t2 - t1, 2)} second(s)")
