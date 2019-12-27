from abc import ABC, abstractmethod
from collections import deque


class Building:

    def __init__(self):
        self.storage = deque()

    def __add__(self, other):
        self.storage = self.storage + other
        return self.storage

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self.storage += other
        return self.storage

    def __str__(self):
        return f"{self.storage}"


class Factory(Building):

    def __init__(self):
        super().__init__()

    @property
    def pop_element(self):
        if len(self.storage) > 0:
            return self.storage.popleft()

        print("Закончились")

class Port(Building):

    def __init__(self):
        super().__init__()

    @property
    def pop_element(self):
        if len(self.storage) > 0:
            return self.storage.popleft()

        print("Закончились")


class Warehouse(Building):

    def __init__(self):
        super().__init__()

    @property
    def pop_element(self):
        if len(self.storage) > 0:
            return self.storage.popleft()

        print("Закончились")


class Transport:

    def __init__(self, route_map, time):

        self.time = time
        self.cargo_on_board = None

    def move_on_route(self, route_map, endpoint, cargo):
        self.route_map = route_map
        self.time_in_rout = 2*route_map[endpoint]
        self.cargo_on_board = cargo


class DispetcherTimeTrasport:

    def __init__(self, transport1, transport2):
        self.transport = (transport1, transport2)
        self.status = None
        self.output = []

    def checking_transport_time(self):
        for rout_situation in self.transport:
            print("transport time: ", rout_situation.time)

            if rout_situation.time == 0 and not self.output:  # It's redy to start
                print("Redy to start")
                self.output.append(rout_situation)

            else:
                print("Does not redy to start")
                self.status = False



class DispetcherBuild:

    def __init__(self, build):
        self.build = (build,)
        self.output = []

    def checking_cargo_in_build(self):
        for each_build in self.build:
            print(each_build.storage)
            if each_build.storage and not self.output:  # It's redy to pop
                print("redy to pop")
                # return True
            else:
                print("Empty storage")
                # return False  # Empty storage

class DispetcherMove:
    def __init__(self, disptime, dispbuild):
        self.dtime = disptime
        self.dbuild = dispbuild

    def start_move(self):
        if self.dtime.output and self.dbuild.output:
            print("Start move")
        else:
            print("Wait")


rout_map = {"A": 1, "B": 5, "Port": 4}

time = 0
while time < 2:

    port = Warehouse()
    port.storage += "AB"

    dispetcherBuild = DispetcherBuild(port)
    dispetcherBuild.checking_cargo_in_build()

    car1 = Transport(rout_map, time=0)
    car2 = Transport(rout_map, time=1)


    dispetcherTime = DispetcherTimeTrasport(car1, car2)
    dispetcherTime.checking_transport_time()

    dispetcherMove = DispetcherMove(dispetcherTime, dispetcherBuild)
    dispetcherMove.start_move()

    time += 1






class Timer:

    def __init__(self, time1, time2, time3):
        self.Truck_1 = time1
        self.Truck_2 = time1
        self.Ship = time3


class Truck(Transport):
    def route(self, element):
        if element == "A":
            print("A")
        else:
            print("B")


class Ship(Transport):
    pass









