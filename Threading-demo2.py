import time
import threading
import concurrent.futures

def do_something(sec):
    print(f'Sleeping for {sec} seconds....')
    time.sleep(1)
    print(f"Sleeping done....{sec}")

t1 = time.perf_counter()

# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
sec = [1,2,3,4,5]
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     result = executor.map(do_something,sec)

# for f in result:
#     print(f)
print('-'*50)
with concurrent.futures.ThreadPoolExecutor() as exe:
    [exe.submit(do_something, i) for i in sec]

    # if your function returns something then collect all the results in a variable and call .result() on top of that
    # for f in concurrent.futures.as_completed(res) :
    #     print(f.result())




t2 = time.perf_counter()

print("total execution time : ", round(t2-t1,2))