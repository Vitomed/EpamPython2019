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


class DispetcherTimeTrasport:

    def __init__(self, transport):
        self.transport = (transport,)

    def checking_transport_time(self):
        for rout_situation in self.transport:
            print(rout_situation.time)
            if rout_situation.time == 0:  # It's redy to start
                return True
            else:
                return False


class DispetcherBuild:

    def __init__(self, build):
        self.build = (build,)

    def checking_cargo_in_build(self):
        for each_build in self.build:
            print(each_build.storage)
            if each_build.storage:  # It's redy to pop
                print("redy to pop")
                return True
            else:
                print("Empty storage")
                return False  # Empty storage


class DispetcherMove:
    def __init__(self):
        pass

# a = "B"
# port = Warehouse()
# dispetcherBuild = DispetcherBuild(port)
# port.storage += "AB"
# print(port.pop_element)
# print(port.pop_element)
# print(dispetcherBuild.checking_cargo_in_build())
# port + deque("B")
# port += deque("C")
# print(port)

rout_map = {"A": 1, "B": 5, "Port": 4}

class Transport:

    def __init__(self, route_map):

        self.time_in_rout = 0
        self.cargo_on_board = None

    def move_on_route(self, route_map, endpoint, cargo):
        self.route_map = route_map
        self.time_in_rout = 2*route_map[endpoint]
        self.cargo_on_board = cargo

car = Transport()


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









