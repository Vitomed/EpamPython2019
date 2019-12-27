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

    def __init__(self, rout_map, time, garage):

        self.time = time
        self.cargo_on_board = None
        self.garage = garage.__class__
        self.rout_map = rout_map
        self.half_path = time//2

    def move_on_route(self, rout_map, endpoint, cargo):
        self.time_in_rout = 2*rout_map[endpoint]
        self.cargo_on_board = cargo

    def put_cargo(self, endpoint):
        endpoint.append(self.cargo_on_board)
        self.cargo_on_board = None

    def set_cargo(self, item):
        self.cargo_on_board = item

class Truck(Transport):
    def __init__(self, rout_map, time, garage):
        super().__init__(rout_map, time, garage)

class Ship(Transport):
    def __init__(self, rout_map, time, garage):
        super().__init__(rout_map, time, garage)

class DispetcherTimeTrasport:

    # def __init__(self, transport1, transport2, sip):
    #     self.transport = (transport1, transport2, sip)
    def __init__(self, transport1):
        self.transport = (transport1,)
        self.status = True
        self.output = []

    def checking_transport_time(self):
        for rout_situation in self.transport:
            print("transport time: ", rout_situation.time)

            # if rout_situation.time == 0 and not self.output:  # It's redy to start
            if rout_situation.time == 0:  # It's redy to start
                print("Redy to start, оповещаем о готовности к отправке")
                self.output.append(rout_situation)
                self.status = True
            elif rout_situation.time == rout_situation.half_path:
                print("Half path")
            else:
                print("Does not redy to start, Меняем время в машине")
                self.status = False

class DispetcherBuild:

    # def __init__(self, factory, port):
    #     self.build = (factory, port)
    def __init__(self, factory):
        self.build = (factory,)
        self.status = None
        self.output = []

    def checking_cargo_in_build(self):
        for each_build in self.build:
            print(each_build.storage)
            # if each_build.storage and not self.output:  # It's redy to pop
            if each_build.storage:  # It's redy to pop
                self.status = True
                print("redy to pop")
                # return True
            else:
                print("Empty storage")
                self.status = False
                # return False  # Empty storage

class DispetcherMove:
    def __init__(self, disptime, dispbuild, transport):
        self.dtime = disptime
        self.dbuild = dispbuild
        self.transport = transport

    def start_move(self):
        print("DispMove", transport.garage)
        # self.transport.set_cargo("A")

    def finish_move(self):
        print("Я доехала до пункта назначения")

builds = {"A": "Factory", "B": "Factory"}

#  У каждого транспорта, своя дорожная карта
rout_map_truck = {"A": 1, "B": 5}
rout_map_ship = {"A": 4}

time = 0


factory = Factory()
factory.storage += "AB"

port = Port()
port.storage += "DC"

car1 = Truck(rout_map_truck, time=0, garage=factory)
car2 = Truck(rout_map_truck, time=1, garage=factory)
ship = Ship(rout_map_ship, time=1, garage=port)

# dispetcherTime = DispetcherTimeTrasport(car1)
# dispetcherBuild = DispetcherBuild(factory)


while time < 2:
    for transport in [car1, car2, ship]:
        dispetcherTime = DispetcherTimeTrasport(transport)
        dispetcherBuild = DispetcherBuild(factory)

        dispetcherTime.checking_transport_time()
        dispetcherBuild.checking_cargo_in_build()
        dispetcherMove = DispetcherMove(dispetcherTime, dispetcherBuild, transport)

        if dispetcherBuild.status and dispetcherTime.status:
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









