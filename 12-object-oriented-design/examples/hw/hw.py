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
    def __init__(self, build_name):
        """

        :param build_name: specific building name
        :param storage: place for storing cargo

        At the initial time, all buildings are created empty, they do not contain cargo
        Later, we can add the necessary initial conditions for finding the cargo by
        applying special concatenation for this class (use case: building_istance + "cargo").
        """
        self.storage = deque()
        self.name = build_name


class Factory(Building):

    def __init__(self, build_name):
        super().__init__(build_name)


class Port(Building):

    def __init__(self, build_name):
        super().__init__(build_name)


class Warehouse(Building):

    def __init__(self, build_name):
        super().__init__(build_name)


class Time:

    def __init__(self):
        """
        :param time_to_endpoint: length of time to the point of discharge
        :param time_come_back:the length of time the vehicle arrives at
        the starting point again
        """

        self.time_to_endpoint = None
        self.time_come_back = 0


class Transport(Time):

    def __init__(self, transport_name, rout_map, garage, endpoint):
        """
        :param transport_name: specific transport name
        :param rout_map: rout map for navigation each vechile
        :param garage: place there vevhile starts move
        :param endpoint: place where need to deliver the goods
        """

        super().__init__()
        self.cargo_on_board = deque()
        self.name = transport_name
        self.garage = garage
        self.endpoint = endpoint
        self.rout_map = rout_map

    def take_cargo_from_garage(self):
        """
        Took the load from the garage
        Now there is cargo on board the vehicle,
        and one container less in storage
        """
        self.cargo_on_board += self.garage.storage.popleft()
        print("Я забрал новый груз и везу его:", self.cargo_on_board)

    def take_rout_settings(self):
        """
        View the roadmap and remember the characteristics
        of the route: The length of the route for cargo on board
        """
        self.time_to_endpoint = self.rout_map[self.cargo_on_board[0]]
        self.time_come_back += self.time_to_endpoint * 2 - 1

    def put_cargo_to_warehouse(self):
        """
        Put the goods upon arrival
        """
        self.endpoint[self.cargo_on_board[0]] += self.cargo_on_board.popleft()


class Truck(Transport):
    def __init__(self, transport_name, rout_map, garage, endpoint):
        super().__init__(transport_name, rout_map, garage, endpoint)


class Ship(Transport):
    def __init__(self, transport_name, rout_map, garage, endpoint):
        super().__init__(transport_name, rout_map, garage, endpoint)


class DispetcherTimeTrasport:

    def __init__(self, transport):

        """
        :param transport: class instance transport
        :param status: signals whether the vehicle is ready to take cargo on board
        """
        self.transport = transport
        self.status = True

    def checking_transport_time(self):

        """
        checks the condition of the vehicle and corrects or maintains status
        and makes a timer change
        """
        print("Статистика для: ", transport.name)
        if transport.time_to_endpoint == 0:  # It's redy to start
            self.status = True  # Готов к новым путешествиям - Да!

        # Я должен быть с грузом, чтобы иметь возможность оставить его на складе
        elif transport.time_to_endpoint == transport.time_come_back and transport.cargo_on_board:
            transport.put_cargo_to_warehouse()
            transport.time_come_back = transport.time_come_back - 1
            self.status = False
            print("Груз доставлен, Ура!")

        # Обнулим время, ведь мы готовы взять другой груз и отправиться в новый маршрут!
        elif transport.time_come_back == 0:
            transport.time_to_endpoint = 0
            self.status = True  # Готов к новым путешествиям - Да!

        #  Нахожусь еще в пути. С грузом или без - это неважно!
        else:
            transport.time_come_back = transport.time_come_back - 1
            self.status = False

        print("Время в конечную точку составляет: ", transport.time_to_endpoint)
        print("Остаток времени до прибытия обратно в гараж: ", transport.time_come_back)


class DispetcherBuildSituation:

    def __init__(self, build):
        """
        :param build: is a garage - warehouse, from where the vehicle receives the goods
        :param status: signals whether the storage is ready cargo has been issued for the vehicle
        """
        self.garage = build
        self.status = None

    def checking_cargo_in_build(self):
        """
        Checks the availability of cargo in the storage and changes the status:
        (Yes - you can receive the cargo, No - the storage is empty)
        """
        print(f"Ситуация в хранилище {self.garage.name}:", self.garage.storage)
        if self.garage.storage:  # It's redy to pop
            self.status = True
            print("redy to pop")
        else:
            self.status = False
            print("Empty storage")


class DispetcherMove:  # Класс, для подстчета контейнеров в гараже и на складе

    """
    This class summarizes the work done and tells us
    when all things are done and the goods are delivered.
    """

    def __init__(self, endpoints, garage):
        """

        :param endpoints: warehouse
        :param garage: storage
        :param count_cargo_in_endpoints: storage
        :param count_cargo_in_garages_: storage
        """
        self.endpoint = endpoints
        self.garage = garage
        self.count_cargo_in_endpoints = {}
        self.count_cargo_in_garages = {}

    def counter(self):
        """
        With each new call, checks the
        amount of goods in the warehouse
        and storage and updates the information
        """
        for endpoint_element in self.endpoint:
            self.count_cargo_in_endpoints[endpoint_element] = len(endpoint_element.storage)

        for garage_element in self.garage:
            self.count_cargo_in_garages[garage_element] = len(garage_element.storage)

# cargo = "A"
# cargo = "AB"
# cargo = "BB"
cargo = "ABB"
factory = Factory("Factory")
factory.storage += cargo

port = Port("Port")

WB = Warehouse("WB")
WA = Warehouse("WA")


#  У каждого типа транспорта, своя дорожная карта
endpoint_Truck = {"A": port, "B": WB}
rout_map_Truck = {"A": 1, "B": 5}

endpoint_Ship = {"A": WA}
rout_map_ship = {"A": 4}

garage = [factory, port]
endpoints = [port, WA, WB]

# garage = [factory]
# endpoints = [port]

truck_1 = Truck(transport_name="Truck_1", rout_map=rout_map_Truck, garage=factory, endpoint=endpoint_Truck)
truck_2 = Truck(transport_name="Truck_2", rout_map=rout_map_Truck, garage=factory, endpoint=endpoint_Truck)
ship = Truck(transport_name="Ship", rout_map=rout_map_ship, garage=port, endpoint=endpoint_Ship)

transports = [truck_1, truck_2, ship]
print("[Start]\n")
count = 1
timer = 0
while count:

    for transport in transports:
        print("count iterations: ", count)
        print(f"timer: {timer} =====================================")

        dispetcherTime = DispetcherTimeTrasport(transport)
        dispetcherBuild = DispetcherBuildSituation(transport.garage)

        dispetcherTime.checking_transport_time()
        dispetcherBuild.checking_cargo_in_build()

        dispetcherMove = DispetcherMove(endpoints, garage)
        dispetcherMove.counter()

        if dispetcherBuild.status and dispetcherTime.status:
            transport.take_cargo_from_garage()
            transport.take_rout_settings()

    if sum(dispetcherMove.count_cargo_in_endpoints.values()) == len(cargo) and not any(
            dispetcherMove.count_cargo_in_garages.values()):
        break
    else:
        timer += 1
print("[Finish]")

print(f"Время доставки груза: {timer}")
print("1 Груз, который сейчас на фабрике: ", factory)
print("2 Груз, который сейчас в порту: ", port)
print("3 Груз, который сейчас в WA: ", WA)
print("4 Груз, который сейчас в WB: ", WB)
