"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.
"""

import yaml
from abc import ABC, abstractmethod


class AbstractProduct(ABC):

    @abstractmethod
    def get_product(self, dish_position):
        pass


class AbstractFactory(ABC):

    @abstractmethod
    def get_first_position(self, today_menu):
        pass

    @abstractmethod
    def get_second_position(self, today_menu):
        pass

    @abstractmethod
    def get_drink(self, today_menu):
        pass


class First(AbstractProduct):

    def __init__(self):
        self.dish_position = "first_courses"

    def get_product(self, today_menu):
        return today_menu[self.dish_position]


class Second(AbstractProduct):

    def __init__(self):
        self.dish_position = "second_courses"

    def get_product(self, today_menu):
        return today_menu[self.dish_position]


class Drink(AbstractProduct):

    def __init__(self):
        self.dish_position = "drinks"

    def get_product(self, today_menu):
        return today_menu[self.dish_position]


class Vegan(AbstractFactory):

    def __init__(self):
        self.tipe_lunch = "vegan"

    def get_first_position(self, today_menu):
        position = First().get_product(today_menu)
        return position[self.tipe_lunch]

    def get_second_position(self, today_menu):
        position = Second().get_product(today_menu)
        return position[self.tipe_lunch]

    def get_drink(self, today_menu):
        position = Drink().get_product(today_menu)
        return position[self.tipe_lunch]


class Children(AbstractFactory):

    def __init__(self):
        self.tipe_lunch = "child"

    def get_first_position(self, today_menu):
        position = First().get_product(today_menu)
        return position[self.tipe_lunch]

    def get_second_position(self, today_menu):
        position = Second().get_product(today_menu)
        return position[self.tipe_lunch]

    def get_drink(self, today_menu):
        position = Drink().get_product(today_menu)
        return position[self.tipe_lunch]


class China(AbstractFactory):

    def __init__(self):
        self.tipe_lunch = "chinese"

    def get_first_position(self, today_menu):
        position = First().get_product(today_menu)
        return position[self.tipe_lunch]

    def get_second_position(self, today_menu):
        position = Second().get_product(today_menu)
        return position[self.tipe_lunch]

    def get_drink(self, today_menu):
        position = Drink().get_product(today_menu)
        return position[self.tipe_lunch]


def client(factory, weekly_menu, day):
    today_menu = weekly_menu[day]
    print(factory.get_first_position(today_menu))
    print(factory.get_second_position(today_menu))
    print(factory.get_drink(today_menu))



if __name__ == "__main__":

    with open("menu.yml", "r") as menu:
        weekly_menu = yaml.safe_load(menu)
    day = "Monday"
    client(Children(), weekly_menu, day)