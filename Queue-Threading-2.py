import queue

'''This is a simple reference script which shows how LIFO and priority queue works'''
q = queue.Queue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())


q1 = queue.LifoQueue()
for i in range(5):
    q1.put(i)

while not q1.empty():
    print(q1.get())

q3 = queue.PriorityQueue()
q3.put((101, 'priority 3'))
q3.put((6595, 'priority 4'))
q3.put((44, 'priority 2'))
q3.put((1, 'priority 1'))

for i in range(q3.qsize()):
    print(q3.get()[1])