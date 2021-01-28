lst = [1,2,3,4,5]
i_num = iter(lst) # by using this iter() we are just converting into iterator object.. or lst.__iter__() will also work
print(i_num) # i_num is now just an iterator
for i in lst :
    print(i)



print(dir(lst)) # dir() will list all the internal magic commands running with the object

# print(next(i_num))
# print(next(i_num))
# print(next(i_num))
# print(next(i_num))
# print(next(i_num))


# instead of for loop we can code this as well. coz internally for loop is handling all these StopIteration exception
while True :
    try :
        item = next(i_num)
        print(item)
    except StopIteration :
        break

def myrange(start, end) :
    curr = start
    while curr < end:
        yield  curr # this method is returning an iterator object
        curr+=1
# NOTE: Generators are also iterators
# an iterable is not an iterator but an iterator is an iterable

print(myrange(1,10))
for i in myrange(1, 10):
    print(i)



