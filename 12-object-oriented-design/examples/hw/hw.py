from abc import ABC, abstractmethod
from collections import deque


class Building:

    # def __init__(self, first_commit=0):
    #
    #     self.first_commit_my_storage = first_commit
    #     self.storage = deque(first_commit)
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

    def __init__(self, rout_map, garage, endpoint):

        self.time_to_endpoint = 0
        self.time_in_rout = 0
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
    def __init__(self, factory):
        self.builds = (factory,)
        self.status = None
        # self.output = []

    def checking_cargo_in_build(self):
        for each_build in self.builds:
            print("Ситуация в хранилище garage", each_build.storage)
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

    def __init__(self, endpoints):
        self.endpoint = endpoints
        self.len_element = {}

    def counter(self):
        for endpoint_element in self.endpoint:
            self.len_element[endpoint_element] = len(endpoint_element.storage)
        print("garage counter", self.len_element)

    def finish_move(self):
        print("Я доехала до пункта назначения")

#  У каждого транспорта, своя дорожная карта
time = 0


factory = Factory()
factory.storage += "AA"
print(factory)

port = Port()
port.storage += ""

WB = Warehouse()
WA = Warehouse()

endpoint_Truck = {"A": port, "B": WB}
rout_map_truck = {"A": 1, "B": 1}

endpoint_Ship = {"A": WA}
rout_map_ship = {"A": 4}

garage = [factory]
endpoints = [port]

car1 = Truck(rout_map_truck, garage=factory, endpoint=endpoint_Truck)
car2 = Truck(rout_map_truck, garage=factory, endpoint=endpoint_Truck)
# ship = Ship(rout_map_ship, time=1, garage=port, endpoint=endpoint_Ship)

# dispetcherTime = DispetcherTimeTrasport(car1)
# dispetcherBuild = DispetcherBuild(factory)

print("[Start While]")
print("\n")
count = 1
while count < 40:

    # for transport in [car1, car2, ship]:
    for transport in [car1, car2]:
        print("count iterations: ", count)
        print("=====================================")
        dispetcherTime = DispetcherTimeTrasport(transport)
        dispetcherBuild = DispetcherBuild(factory)

        dispetcherTime.checking_transport_time()
        dispetcherBuild.checking_cargo_in_build()

        dispetcherMove = DispetcherMove(endpoints)
        dispetcherMove.counter()

        print("len AA", len("AA"))
        print(sum(dispetcherMove.len_element.values()))
        print(sum(dispetcherMove.len_element.values()) == len("AA"))

        if dispetcherBuild.status and dispetcherTime.status:
            transport.move_on_route()

            print("// Груз, который сейчас на фабрике", factory)
            print("=====================================")


    if sum(dispetcherMove.len_element.values()) == len("AA"):
        print("Закончили на итерации", count)
        print(sum(dispetcherMove.len_element.values()) == len("AA"))
        break

    count += 1

print("3 Груз, который сейчас на фабрике", factory)
print("4 Груз, который пришел в порт", port)
print("[Finish while]")










