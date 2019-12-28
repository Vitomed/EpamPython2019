from abc import ABC, abstractmethod
from collections import deque


class MixIn:

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


class Building(MixIn):
    # def __init__(self, first_commit=0):
    #
    #     self.first_commit_my_storage = first_commit
    #     self.storage = deque(first_commit)
    def __init__(self):
        self.storage = deque()


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


class Time:

    def __init__(self, one, two):
        self.time_to_endpoint = one
        self.time_in_rout = two

class Transport(Time):

    def __init__(self, rout_map, garage, endpoint):
        super().__init__(one=0, two=0)
        # self.time_to_endpoint = 0
        # self.time_in_rout = 0
        self.cargo_on_board = deque()

        self.garage = garage
        self.rout_map = rout_map
        self.endpoint = endpoint

    def move_on_route(self):
        print("Я пустой и нахожусь в гараже: ", self.cargo_on_board)
        self.cargo_on_board += self.garage.storage.popleft()
        print("А теперь я забрал груз и везу его:", self.cargo_on_board)
        self.time_to_endpoint = self.rout_map[self.cargo_on_board[0]]
        self.time_in_rout = self.time_to_endpoint * 2
        print("Время в конечную точку составляет: ", self.time_to_endpoint)
        print("До того, как вернуться обратно осталось: ", self.time_in_rout)


    def put_cargo(self):
        self.endpoint[self.cargo_on_board[0]] += self.cargo_on_board
        print(self.endpoint[self.cargo_on_board[0]])
        self.cargo_on_board = deque()
        print(f"Освободилась от груза, теперь он появился в конечной точке {self.endpoint.__class__}")
        print(f"Сколько прошло времени, должно быть ровно 1/2 времени на маршрут: {self.time_in_rout}")



class Truck(Transport):
    def __init__(self, rout_map, garage, endpoint):
        super().__init__(rout_map, garage, endpoint)


class Ship(Transport):
    def __init__(self, rout_map, garage, endpoint):
        super().__init__(rout_map, garage, endpoint)

class DispetcherTimeTrasport:

    # def __init__(self, transport1, transport2, sip):
    #     self.transport = (transport1, transport2, sip)
    def __init__(self, transport1, ):
        self.transport = (transport1,)
        self.status = True
        # self.output = []

    def checking_transport_time(self):
        for rout_situation in self.transport:
            print("transport class", rout_situation.__class__)

            # if rout_situation.time == 0 and not self.output:  # It's redy to start
            if rout_situation.time_to_endpoint == 0:  # It's redy to start
                print("Redy to start, оповещаем о готовности к отправке")
                self.status = True  # Готов к новым путешествиям - Да!

            elif rout_situation.time_to_endpoint == rout_situation.time_in_rout and rout_situation.cargo_on_board:
                rout_situation.put_cargo()
                print("Груз доставлен")
                self.status = False

            elif rout_situation.time_in_rout == 0:
                print("Обнулим время time to endpoint")
                rout_situation.time_to_endpoint = 0
                self.status = True  # Готов к новым путешествиям - Да!

            else:
                print("Я еще не вернулся обратно, меняем время в машине")
                rout_situation.time_in_rout = rout_situation.time_in_rout - 1
                self.status = False

            print("Checking time")
            print("time to endpoint: ", rout_situation.time_to_endpoint)
            print("До того, как вернуться обратно осталось: ", rout_situation.time_in_rout)


class DispetcherBuild:

    # def __init__(self, factory, port):
    #     self.build = (factory, port)
    def __init__(self, build):
        self.builds = (build,)
        self.status = None
        # self.output = []

    def checking_cargo_in_build(self):
        for each_build in self.builds:
            print("Ситуация в хранилище garage", each_build.__class__, each_build.storage)
            # if each_build.storage and not self.output:  # It's redy to pop

            if each_build.storage:  # It's redy to pop
                self.status = True
                print("redy to pop")
                return True

            else:
                print("Empty storage")
                self.status = False
                # return False  # Empty storage

class DispetcherMove:  # Класс, для учета времени доставки

    def __init__(self, endpoints, garage):
        self.endpoint = endpoints
        self.garage = garage
        self.len_element_endpoints = {}
        self.len_element_garage = {}

    def counter(self):
        for endpoint_element in self.endpoint:
            self.len_element_endpoints[endpoint_element] = len(endpoint_element.storage)
        print("garage counter", self.len_element_endpoints)
        for garage_element in self.garage:
            self.len_element_garage[garage_element] = len(garage_element.storage)

#  У каждого транспорта, своя дорожная карта

cargo = "AA"
factory = Factory()
factory.storage += cargo
print(factory)

port = Port()
# port.storage += ""

WB = Warehouse()
WA = Warehouse()

endpoint_Truck = {"A": port, "B": WB}
rout_map_truck = {"A": 1, "B": 1}

endpoint_Ship = {"A": WA}
rout_map_ship = {"A": 4}

garage = [factory, port]
endpoints = [port, WA]

car1 = Truck(rout_map_truck, garage=factory, endpoint=endpoint_Truck)
# car2 = Truck(rout_map_truck, garage=factory, endpoint=endpoint_Truck)
ship1 = Ship(rout_map_ship, garage=port, endpoint=endpoint_Ship)
ship2 = Ship(rout_map_ship, garage=port, endpoint=endpoint_Ship)


print("[Start While]")
print("\n")
count = 1
while count < 20:

    # for transport in [car1, ship1, ship2]:
    for transport in [car1]:
        print("count iterations: ", count)
        print("=====================================")
        dispetcherTime = DispetcherTimeTrasport(transport)
        dispetcherBuild = DispetcherBuild(transport.garage)

        dispetcherTime.checking_transport_time()
        dispetcherBuild.checking_cargo_in_build()

        dispetcherMove = DispetcherMove(endpoints, garage)
        dispetcherMove.counter()

        # print("len AA", len("AA"))
        # print(sum(dispetcherMove.len_element_endpoints.values()))
        # print(sum(dispetcherMove.len_element_endpoints.values()) == len(cargo))

        if dispetcherBuild.status and dispetcherTime.status:
            transport.move_on_route()

            print("// Груз, который сейчас на фабрике", factory)
            print("=====================================")


    if sum(dispetcherMove.len_element_endpoints.values()) == len("AA") and not any(dispetcherMove.len_element_garage.values()):
        print("Закончили на итерации", count)
        print(sum(dispetcherMove.len_element_endpoints.values()) == len("AA"))
        break

    count += 1

print("3 Груз, который сейчас на фабрике", factory)
print("4 Груз, который пришел в порт", port)
print("[Finish while]")










