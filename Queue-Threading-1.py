import queue, time
import threading
'''This is a basic reference script that shows how to use Queues & different types of Queues in python
   There are basically 3 types of Queues :-
   1. FIFO (default)
   2. LIFO
   3. Priority
'''


# q = queue.Queue()
# q.put(5)

# print(q.get()) # to fetch the items in the Queue

# print(q.empty()) # once we fetch the object from the queue the item is removed automatically from the queue

# for i in range(1,5):
#     print('inserting inside queue ....{} \n'.format(i))
#     q.put(i)


# while not q.empty():
#     '''Always use q.empty() otherwise if you are using single thread only then if there are no items in the queue then your queue will
#        get freezed and it will wait till next items comes in the queue. So , ALWAYS USE DIFFERENT THEREADS TO ACCESS THE 1 QUEUE
#     '''
#     print(q.get(), end=' ')

def putting_thread(q):
    while True:
        print('Starting thread \n')
        time.sleep(10)
        q.put(5)
        print('put something \n')

q = queue.Queue()
t = threading.Thread(target=putting_thread, args=(q,), daemon=True) # make it a daemon thread so main func finished automatically daemon thread will also finish
t.start()

q.put(55)
print('first item gotten \n')
# while True:
#     print(q.get())
#     print('finished')

