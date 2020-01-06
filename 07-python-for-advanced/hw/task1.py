"""
Реализовать такой метакласс, что экземпляры класса созданного с помощью него
будут удовлетворять следующим требованиям:

* объекты созданные с одинаковыми аттрибутами будут одним и тем же объектом
* объекты созданные с разными аттрибутами будут разными объектами
* у любого объекта есть мозможность получить доступ к другим объектам
    того же класса


# >>> unit1 = SiamObj('1', '2', a=1)
# >>> unit2 = SiamObj('1', '2', a=1)
# >>> unit1 is unit2
# True
# >>> unit3 = SiamObj('2', '2', a=1)
# >>> unit3.connect('1', '2', 1).a = 2
# >>> unit2.a == 2
# True
# >>> pool = unit3.pool
# >>> print(len(pool))
# 2
# >>> del unit3
# >>> print(len(pool))
# 1

"""

import weakref
import inspect


class SingletonCahceMeta(type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.__cache = weakref.WeakValueDictionary()
        cls.pool = weakref.WeakSet()

    def __call__(cls, *args, **kwargs):

        key_signature = str(inspect.signature(
            cls.__init__).bind_partial(cls, *args, **kwargs))
        if key_signature in cls.__cache:
            return cls.__cache[key_signature]
        else:
            obj = super().__call__(*args, **kwargs)
            cls.connect = connect
            cls.pool.add(obj)

            cls.__cache[key_signature] = obj
            return obj


def connect(cls, *args, **kwargs):

    key_signature = str(inspect.signature(
        cls.__init__).bind_partial(cls, *args, **kwargs))

    try:
        return cls.__cache[key_signature]
    except AttributeError:
        raise AttributeError("Object with this attribute set is missing")


class Spam(metaclass=SingletonCahceMeta):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


# a = Spam(1, 2, q=12)
b = Spam(1, 2, 4)
# del b
d = Spam(4, 5, 6)
a = Spam(4, 5, 6)

# print(a is b)
# print(a is d)
# print(a._SingletonCahceMeta__cache)
# b.connect(4, 5, 6).b = 7
# print(d.b == 7)

pool = b.pool
print(pool)
print(len(pool))
del b
print(len(pool))
