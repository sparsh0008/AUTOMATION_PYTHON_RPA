# Import Modules
from threading import *
import time


# Class created
class Mythread:
    def tasks(self):
        self.task1()  # Function Call
        self.task2()  # Function Call
        self.task3()  # Function Call

    # Function Define
    def task1(self):
        print("Step 1 of My Problem")
        time.sleep(5)
        print("Step 1 Completed")

    # Function Define
    def task2(self):
        print("Step 2 of My Problem")
        time.sleep(5)
        print("Step 2 Completed")

    # Function Define
    def task3(self):
        print("Step 3 of My Problem")
        time.sleep(5)
        print("Step 3 Completed")


# Single Thread
obj = Mythread()  # Object Creation for Class Mythread()
th = Thread(target=obj.tasks)  # Claas Thread From threading Module
th.start()  # Initiate the Thread
