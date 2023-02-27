from threading import *
from time import *


class Railway:  # If you created a class
    def __init__(self, available):  # constructor is created
        self.available = available

    def reserve(self, wanted):  # Reserve Seats
        name = current_thread().name
        if self.available >= wanted:  # This is to check seats are available or not
            self.available = self.available - wanted  # This will decrease number of seats
            print("Seat is Available for {0}".format(name))
        else:
            print("Seat are not Available for {0}".format(name))


obj = Railway(1)  # available seat

T1 = Thread(target=obj.reserve, args=(1,), name="First Person")  # Operate First Person
T2 = Thread(target=obj.reserve, args=(1,), name="Second Person")  # Operate Second Person
T3 = Thread(target=obj.reserve, args=(1,), name="Third Person")  # Operate Third Person

T1.start()  # Initiate the Thread for First Person
T2.start()  # Initiate the Thread for Second Person
T3.start()  # Initiate the Thread for Third Person
