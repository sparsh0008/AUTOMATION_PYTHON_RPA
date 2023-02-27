# Thread Communication Using Boolean Type Variable

from threading import *
from time import *


class producer:
    def __init__(self):
        self.lst = []
        self.dataproduce = False

    def produce(self):
        for i in range(1, 11):
            self.lst.append(i)
            sleep(1)
            print("Item produced........")
        self.dataproduce = True


class consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        while not self.prod.dataproduce:
            sleep(0.1)
            print(self.prod.lst)
            # print("Consumption Is Going On")


p = producer()
c = consumer(p)

th1 = Thread(target=p.produce)
th2 = Thread(target=c.consume)
th1.start()
th2.start()


