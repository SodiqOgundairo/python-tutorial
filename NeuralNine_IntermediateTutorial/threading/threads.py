# threading
# threading is a way to run multiple threads (tasks, function calls) at the same time.
# Python has a built-in threading module to work with threads.

import threading
import time


def function1():
    for x in range(20):
        print('ONE')


def function2():
    for x in range(20):
        print('TWO')


t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
t2.start()

t1.join()  # wait until thread 1 is completely executed
t2.join()  # wait until thread 2 is completely executed

print('\n\nDONE\n\n')


# thread synchronization using locks
# A lock is a synchronization primitive that is used to protect shared resources from being accessed by multiple threads at the same time.
# This is important because if multiple threads access the same resource at the same time, it can lead to data corruption or other unexpected behavior.
x = 8192

lock = threading.Lock()


def double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(0.5)  # sleep for 0.5 seconds just to simulate a delay
    print('Reached maximum value\n\n')
    lock.release()


def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(0.5)  # sleep for 0.5 seconds just to simulate a delay
    print('Reached minimum value\n\n')
    lock.release()


t3 = threading.Thread(target=halve)
t4 = threading.Thread(target=double)

t3.start()
t4.start()


# semaphores
# A semaphore is a synchronization primitive that is used to control access to a shared resource by multiple threads.
# A semaphore maintains a count of the number of threads that are currently accessing the shared resource.
# When a thread wants to access the shared resource, it must acquire the semaphore.
# If the semaphore's count is greater than zero, the thread is allowed to access the resource and the count is decremented.
# If the count is zero, the thread is blocked until another thread releases the semaphore and increments the count.

semaphore = threading.BoundedSemaphore(5)


def access(thread_number):
    print(f'{thread_number} is trying to acces the resource')
    semaphore.acquire()
    print(f'{thread_number} has accessed the resource')
    time.sleep(10)  # simulate a delay
    print(f'{thread_number} is releasing the resource')
    semaphore.release()


for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,)).start()
    time.sleep(1)
