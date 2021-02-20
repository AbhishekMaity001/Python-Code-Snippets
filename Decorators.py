import time
import numpy as np

def div(a,b):
    print( a/b)

def smart(func):
    def inner(a,b):
        if a<b :
            a,b = b,a
        return func(a,b)
    return inner

def measure_time(func):
    def tm(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Total time taken {} seconds'.format((end-start)*1000))
        return result
    return tm

@measure_time
def cnt(lst):
    result = []
    for i in range(len(lst)):
        result.append(i*i)
    return result

if __name__ == '__main__':
    # div(5,40)
    # abc = smart(div)
    # abc(6,60)
    a = np.arange(1,1000000)
    cnt(a)
