# Collections
import collections
from collections import Counter

#Containers
#list
#set
#dict
#tuple - immuttable

#Types
# 1.counter
# 2.deque
# 3. namedTuple
# 4. orderDict
# 5. defaultDict

c = Counter('abhishek')
print(c)
c = Counter([1,2,3,3,4,4,5,5,5])
print(c)
c = Counter({"a" : 1, "a" : 2, "b" : 3})
print(c)
c = Counter(cats=4, dogs=41)
print(list(c.elements()))
print(c.most_common(1))