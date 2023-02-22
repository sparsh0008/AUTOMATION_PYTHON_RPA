from threading import *
from time import *
from queue import *


class producer:
    def __init__(self):
        self.q = Queue()

    def produce(self):
        for i in range(1, 11):
            print("Producing item: ", i)
            self.q.put(i)
            sleep(1)


class consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        for i in range(1, 11):
            print("Receiving Item", self.prod.q.get(i))
            print("\n")


p = producer()
c = consumer(p)

th1 = Thread(target=p.produce)
th2 = Thread(target=c.consume)

th1.start()
th2.start()
