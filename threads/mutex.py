'''
    Mutex is used for thread synchronization in race condition for a single thread entry
'''

from threading import *
from time import *

def display(str1):
    l.acquire()
    for x in str1:
        print(x)
    l.release()

l = Lock()

t1 = Thread(target=display, args=('HELLO WORLD',))
t2 = Thread(target=display, args=('you are welcome',))

t1.start()
t2.start()

t1.join()
t2.join()

# Using the lock whichever thread acquires the function first will run fully then the other thread