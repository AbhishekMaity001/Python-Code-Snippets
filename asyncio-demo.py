"""
    THIS SCRIPT IS JUST A SIMPLE REFERENCE ON HOW asyncio MODULE WORKS IN PYTHON !!!
"""

import asyncio
import time

async def main():
    """
        1. Every async function returns a COROUTINE object that must be awaited inside the async function only!!
        2. To run just Define an async event-loop is a design pattern that waits for & dispatches events or messages in a program
    """
    # print('Inside the main printing the main')
    # await foo('This is inside the foo function...')
    # print('finished the function above')
    # # now till here the function will run normally ie... synchronously

    print('Inside the Main() function...')
    task = asyncio.create_task(foo('Inside Foo() function! ')) # created a task & passed a coroutine foo
    # await task # this line will block the above task untill executed completely
    await asyncio.sleep(0.5)
    print('This is end of the main() function')

async def foo(text):
    print(text)
    await asyncio.sleep(5) # you will create a co routine and execute with await keyword (await will always be inside async function)
    

# RuntimeWarning: Enable tracemalloc to get the object allocation traceback (when you run only the async function!!)
# print(main()) 

# await must be used inside the function !! you need to create a async event-loop
# await main()

"""THIS IS A SAMPLE USECASE SHOWING 2 FUNCTIONS."""
# This function will just fetch something that will take lets say 2 seconds time then return the data dictionary!
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data' : 99999}

# This function will continously print 10 numbers whenever called.
async def print_nums():
    for i in range(1,11):
        print("The number is ==> {}".format(i))
        await asyncio.sleep(1)

async def main2():
    """
         So , Basically what is hapenning here is when you are creating task 1 then the program is seeing that it is taking 2 secs time
         so it will give the control to task 2 of the program then task 2 will be executing continously (bcoz we are awaited by task 2)
         then while task 2 is printing ... task 1 (which was scheduled earlier will keep a poll that whenever it is completed it will
         just return the value)
    """

    # When you create a task and the coroutine inside that task returns a value then it will create a Future (Future is a kind of place holder that tells that some value will exist in future)
    task1 = asyncio.create_task(fetch_data()) 
    task2 = asyncio.create_task(print_nums())

    value = await task1 # Now we are making sure that the task1 that will return the value then only move forward in the program to end it
    print('value is ::', value)
    await task2 # awaiting for task 2 also to complete only after then "EXIT" the whole script!
    

# pass a COROUTINE inside the run (*****COROUTINE is any function that has async def******)
asyncio.run(main2()) # asyncio just created an event loop and placed that co-routine to run!! Here main2 is the co-routine


