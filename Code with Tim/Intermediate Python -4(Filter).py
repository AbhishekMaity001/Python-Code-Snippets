# Filter function is similar to the map function but the main difference is that
# Map function will get applied to all the items in a list or any object
# Filter function will only get applied to only the True values returned from list or any object

lst = [1,2,3,4,5,6,7,8,9,10]

def createlist(x):
    return x*2
def checkeven(x) :
    return x %2 ==0

print(list(map(createlist, filter(checkeven, lst))))





