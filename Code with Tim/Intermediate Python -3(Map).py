li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x*x
print(list(map(func, li))) # map function ...it applies a function to every item in a list or any iterable
x = [func(i) for i in li] # list comprehension
print(x)
