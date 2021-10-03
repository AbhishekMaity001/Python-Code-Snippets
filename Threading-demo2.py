from concurrent.futures.process import EXTRA_QUEUED_CALLS
import time
import threading
import concurrent.futures # Latest method of doing threading

# Any Function which is consuming some amount of time
def do_something(sec):
    print(f'Sleeping for {sec} seconds....')
    time.sleep(sec)
    # print(f"Sleeping done....{sec}")
    return f"Sleeping done .. {sec}"

t1 = time.perf_counter() # Start time

'''
    If you want to execute a method once at a time then use the submit method on the executor, Submit method places a function to be 
    executed and returns a future Object! The future Object basically encapsulates the execution of the function & also allows us to 
    check the state of the function once it is scheduled ie.. it is running or done etc. and also check the result. & if you grab the
    result then it will give you the return value of the function.
'''
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)
#     f3 = executor.submit(do_something, 1)
#     print(f1.result())
#     print(f2.result())
#     print(f3.result())

# with concurrent.futures.ThreadPoolExecutor() as exe:
#     seconds_list = [5,4,3,2,1]
#     results = [exe.submit(do_something, s) for s in seconds_list]
    
#     for f in concurrent.futures.as_completed(results): # as_completed will give you a generator object and yield the values of threads as they are completed!
#         print(f.result())


# Using the map method to run a entire function over a list of values
with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds_list = [5,4,3,2,1]
    results = executor.map(do_something,seconds_list) # when you use the submit method then it returns the future object but when you use map then it returns result directly.
    
    # This will return the order by which they were started (all will be started concurrently only) but returns as they were scheduled!
    for result in results: # this loop is just optional!! 
        print(result, '\n')

    # NOTE : if any exception is there then it won't raise the exception while executing the threads!! 
    #        it will raise the exception while looping through the results so, you can put them in try catch block.









t2 = time.perf_counter()

print("total execution time : ", round(t2-t1,2))