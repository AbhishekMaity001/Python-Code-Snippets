import time

# def square_num(nums):
#     result =[]
#     #time.sleep(1)
#     for i in nums :
#         result.append(i*i)
#     return result
# t1 = time.perf_counter()
# my_nums = square_num([1,2,3,4,5])
# t2 = time.perf_counter()
# print(my_nums)
# print(round(t2-t1,5), 'seconds')


def square_num(nums):
    for i in nums:
        yield (i*i)
# result = square_num([1,2,3,4,5])


# list comprehension
result = (x*x for x in range(1,10)) # use (round braces) for the generators!
# Generators will give you performance boost memory as well as speed because it dosent stores in the memory it yields
# results one by one

print(result)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# Better to use the forloop bcoz it knows when to stop the iteration

for i in result:
    print(i)


# Solving fibonacci using generators!
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(40)
for i in fib:
    print(i)