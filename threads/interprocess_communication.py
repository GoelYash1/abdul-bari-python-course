from queue import Queue
from threading import Lock, Thread, Condition
from time import sleep

"""
    WITH LOCK
"""
# class MyData:
#     def __init__(self):
#         self.data = 0
#         self.flag = False
#         self.lock = Lock()
#
#     def put(self, d):
#         while self.flag:
#             pass
#
#         self.lock.acquire()
#         self.data = d
#         self.flag = True
#         self.lock.release()
#         sleep(1)
#
#     def get(self):
#         while not self.flag:
#             pass
#         self.lock.acquire()
#         x = self.data
#         self.flag = False
#         self.lock.release()
#         sleep(1)
#         return x

"""
    Using Condition
"""
# class MyData:
#     def __init__(self):
#         self.data = 0
#         self.cv = Condition()
#
#     def put(self, d):
#         self.cv.acquire()
#         self.cv.wait(timeout=0)
#         self.data = d
#         self.cv.notify()
#         self.cv.release()
#         sleep(1)
#
#     def get(self):
#         self.cv.acquire()
#         self.cv.wait(timeout=0)
#         x = self.data
#         self.cv.notify()
#         self.cv.release()
#         sleep(1)
#         return x

"""
    Using Queue
"""
q = Queue()
def producer(q):
    i = 1
    while True:
        q.put(i)
        print("Producer:",i)
        sleep(1)
        i+=1

def consumer(q):
    while True:
        x = q.get()
        print("Consumer:",x)
        sleep(1)


t1 = Thread(target=lambda:producer(q))
t2 = Thread(target=lambda:consumer(q))

t1.start()
t2.start()

t1.join()
t2.join()


