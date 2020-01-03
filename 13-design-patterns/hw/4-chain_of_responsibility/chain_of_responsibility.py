"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""
from abc import abstractmethod, ABC


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        """interface for constructing a chain of handlers
        """
        pass

    @abstractmethod
    def handle(self, request):
        """interface to execute the request
        """
        pass


class BaseHandler(Handler):

    #  field for storing the link to the next handler in the chain
    _next_handler = None

    def set_next(self, handle: Handler) -> Handler:
        self._next_handler = handle
        return handle

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)


EGGS_RECIPE = 2
FLOUR_RECIPE = 300
MILK_RECIPE = 0.5
SUGAR_RECIPE = 100
FLOWER_OIL_RECIPE = 10
BUTTER_OIL_RECIPE = 120


class FoodFrige:

    __slots__ = ["eggs_weight", "flour_weight", "milk_weight",
                 "sugar_weight", "flower_oil_weight", "butter_oil_weight"]

    def __init__(self, eggs, flour, milk, sugar, flower_oil, butter_oil):
        self.eggs_weight = eggs
        self.flour_weight = flour
        self.milk_weight = milk
        self.sugar_weight = sugar
        self.flower_oil_weight = flower_oil
        self.butter_oil_weight = butter_oil


class EggsHandler(BaseHandler):
    def handle(self, food_fridge: FoodFrige):
        if food_fridge.eggs_weight < EGGS_RECIPE:
            add_weight = EGGS_RECIPE - food_fridge.eggs_weight
            print(f"Для приготовления блинов нехватает {add_weight} шт яиц")
        if self._next_handler:
            return self._next_handler.handle(food_fridge)


class FlourHandler(BaseHandler):
    def handle(self, food_fridge: FoodFrige):
        if food_fridge.flour_weight < FLOUR_RECIPE:
            add_weight = FLOUR_RECIPE - food_fridge.flour_weight
            print(f"Для приготовления блинов нехватает {add_weight} гр муки")
        if self._next_handler:
            return self._next_handler.handle(food_fridge)


class MilkHandler(BaseHandler):
    def handle(self, food_fridge: FoodFrige):
        if food_fridge.milk_weight < MILK_RECIPE:
            add_weight = MILK_RECIPE - food_fridge.milk_weight
            print(f"Для приготовления блинов нехватает {add_weight} л молока")
        if self._next_handler:
            return self._next_handler.handle(food_fridge)


class SugarHandler(BaseHandler):
    def handle(self, food_fridge: FoodFrige):
        if food_fridge.sugar_weight < SUGAR_RECIPE:
            add_weight = SUGAR_RECIPE - food_fridge.sugar_weight
            print(f"Для приготовления блинов нехватает {add_weight} гр сахара")
        if self._next_handler:
            return self._next_handler.handle(food_fridge)


class SunflowerOilHandler(BaseHandler):
    def handle(self, food_fridge: FoodFrige):
        if food_fridge.flower_oil_weight < FLOWER_OIL_RECIPE:
            add_weight = FLOWER_OIL_RECIPE - food_fridge.flower_oil_weight
            print(f"Для приготовления блинов нехватает {add_weight} мл подсолнечного масла")
        if self._next_handler:
            return self._next_handler.handle(food_fridge)


class ButterHandler(BaseHandler):
    def handle(self, food_fridge: FoodFrige):
        if food_fridge.butter_oil_weight < BUTTER_OIL_RECIPE:
            add_weight = BUTTER_OIL_RECIPE - food_fridge.butter_oil_weight
            print(f"Для приготовления блинов нехватает {add_weight} гр сливочного масла")
        if self._next_handler:
            return self._next_handler.handle(food_fridge)


if __name__ == "__main__":
    food_fridge = FoodFrige(
        eggs=0,
        flour=100,
        milk=0,
        sugar=1000,
        flower_oil=0,
        butter_oil=100
    )

    eggs_handler = EggsHandler()
    flour_handler = FlourHandler()
    milk_handler = MilkHandler()
    sugar_handler = SugarHandler()
    flower_oil_handler = SunflowerOilHandler()
    butter_oil_handler = ButterHandler()

    eggs_handler.set_next(flour_handler)
    flour_handler.set_next(milk_handler)
    milk_handler.set_next(butter_oil_handler)
    butter_oil_handler.set_next(sugar_handler)
    sugar_handler.set_next(flower_oil_handler)
    eggs_handler.handle(food_fridge)

