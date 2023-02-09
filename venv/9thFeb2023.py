# Import modules for working with threads
from threading import *


# Creating a thread without using a class
def display(s):
    print(s + " Sparsh Khanna")


for i in range(5):
    t = Thread(target=display, args=('Hello',))
    t.start()


# Creating a thread by creating a subclass to thread class
class MyThread(Thread):
    def run(self):
        for numbers in range(5):
            print(numbers)


ThreadObj = MyThread()
ThreadObj.start()
ThreadObj.join()


# Creating a thread without creating a subclass to thread class
class MyThread(Thread):
    def __init__(self, s):
        Thread.__init__(self)
        # super().__init__()
        self.s = s

    def run(self):
        print(self.s)


ThreadObj = MyThread('hello')
ThreadObj.start()
ThreadObj.join()
