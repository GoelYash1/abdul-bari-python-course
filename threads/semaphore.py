'''
    Semaphore is used for thread synchronization in race condition for one or more threads at a time
'''

from threading import *
from time import *

def display(str1):
    l.acquire()
    for x in str1:
        print(x)
    l.release()

l = Semaphore(2) # in this more then one thread can enter if I set Semaphore(1) to Semaphore(2) or more any n

t1 = Thread(target=display, args=('HELLO WORLD',))
t2 = Thread(target=display, args=('you are welcome',))
t3 = Thread(target=display, args=('0123456789',))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
