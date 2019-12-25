"""
Реализовать класс Quaternion, позволяющий работать с кватернионами
https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD
Функциональность (магическими методами):
- сложение
- умножение
- деление
- сравнение
- нахождение модуля
- строковое представление и repr
По желанию:
- взаимодействие с числами других типов
"""
import math

class Quaternion:

    __slots__ = ["a", "b", "c", "d"]

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        if isinstance(other, Quaternion):
            new_a = self.a + other.a
            new_b = self.b + other.b
            new_c = self.c + other.c
            new_d = self.d + other.d
            new_Q = Quaternion(new_a, new_b, new_c, new_d)
        elif isinstance(other, (int, float)):
            new_a = self.a + other
            new_Q = (new_a, self.b, self.c, self.d)
        else:
            raise TypeError("Undefined obj")
        return new_Q

    def __sub__(self, other):  # вычитание
        pass

    def __mul__(self, other):  # умножение
        pass

    def __truediv__(self, other):  # деление
        pass

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d

    def __ne__(self, other):
        return not self.__eq__(other)

    def __abs__(self):
        return math.sqrt(pow(self.a, 2) + pow(self.b, 2) + pow(self.c, 2) + pow(self.d, 2))

    def __str__(self):
        pass

    def __repr__(self):
        pass

    pass

a = (1,2,3,4)
b = (1,2,3,4)
q1 = Quaternion(*a)
q2 = Quaternion(*b)
res = q1 + q2

print(abs(q1))
print(abs(q2))
print(res)
