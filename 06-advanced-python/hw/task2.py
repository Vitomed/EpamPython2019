"""
Реализовать класс Quaternion, позволяющий работать с кватернионами
https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD
Функциональность (магическими методами):
- сложение +
- умножение
- деление
- сравнение +
- нахождение модуля +
- строковое представление и repr +
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
        if isinstance(other, (int, float)):
            new_a = self.a + other
            new_Q = Quaternion(new_a, self.b, self.c, self.d)

        elif isinstance(other, Quaternion):
            new_a = self.a + other.a
            new_b = self.b + other.b
            new_c = self.c + other.c
            new_d = self.d + other.d
            new_Q = Quaternion(new_a, new_b, new_c, new_d)

        else:
            raise TypeError("Undefined type")
        return new_Q

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.a += other

        elif isinstance(other, Quaternion):
            self.a += other.a
            self.b += other.b
            self.c += other.c
            self.d += other.d

        else:
            raise TypeError("Undefined type")

    def __sub__(self, other):  # вычитание

        if isinstance(other, (int, float)):
            new_a = self.a - other
            new_Q = Quaternion(new_a, self.b, self.c, self.d)

        elif isinstance(other, Quaternion):
            new_a = self.a - other.a
            new_b = self.b - other.b
            new_c = self.c - other.c
            new_d = self.d - other.d
            new_Q = Quaternion(new_a, new_b, new_c, new_d)

        else:
            raise TypeError("Undefined type")
        return new_Q

    def __rsub__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __mul__(self, other):  # умножение
        if isinstance(other, (int, float)):
            new_a = self.a * other
            new_b = self.b * other
            new_c = self.c * other
            new_d = self.d * other

        elif isinstance(other, Quaternion):

            new_a = (self.a * other.a - self.b * other.b -
                     self.c * other.c - self.d * other.d)

            new_b = (self.a * other.b - self.b * other.a +
                     self.c * other.d - self.d * other.c)

            new_c = (self.a * other.c - self.b * other.d +
                     self.c * other.a - self.d * other.b)

            new_d = (self.a * other.d + self.b * other.c -
                     self.c * other.b + self.d * other.a)
        else:
            raise TypeError("Undefined obj")
        return Quaternion(new_a, new_b, new_c, new_d)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):  # умножение с присваиванием
        if isinstance(other, (int, float)):
            self.a *= other
            self.b *= other
            self.c *= other
            self.d *= other

        elif isinstance(other, Quaternion):

            new_a = (self.a * other.a - self.b * other.b -
                     self.c * other.c - self.d * other.d)

            new_b = (self.a * other.b - self.b * other.a +
                     self.c * other.d - self.d * other.c)

            new_c = (self.a * other.c - self.b * other.d +
                     self.c * other.a - self.d * other.b)

            new_d = (self.a * other.d + self.b * other.c -
                     self.c * other.b + self.d * other.a)
        else:
            raise TypeError("Undefined obj")
        return Quaternion(new_a, new_b, new_c, new_d)

    def __truediv__(self, other):  # деление
        if isinstance(other, (int, float)):
            new_a = self.a / other
            new_b = self.b / other
            new_c = self.c / other
            new_d = self.d / other

        elif isinstance(other, Quaternion):

            new_a = (self.a * other.a - self.b * other.b -
                     self.c * other.c - self.d * other.d)

            new_b = (self.a * other.b - self.b * other.a +
                     self.c * other.d - self.d * other.c)

            new_c = (self.a * other.c - self.b * other.d +
                     self.c * other.a - self.d * other.b)

            new_d = (self.a * other.d + self.b * other.c -
                     self.c * other.b + self.d * other.a)
        else:
            raise TypeError("Undefined obj")
        return Quaternion(new_a, new_b, new_c, new_d)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d

    def __ne__(self, other):
        return not self.__eq__(other)

    def __abs__(self):
        return math.sqrt(pow(self.a, 2) + pow(self.b, 2) + pow(self.c, 2) + pow(self.d, 2))

    def __str__(self):
        return f"a = {self.a}, b = {self.b}, c = {self.c}, d = {self.d}"

    def __repr__(self):
        return f"Quaternion({self.a}, {self.b}, {self.c}, {self.d})"


a = (1, 2, 3, 4)
b = (1, 2, 3, 4)
q1 = Quaternion(*a)
q2 = Quaternion(*b)
res = q1 + 5

# print(abs(q1))
# print(abs(q2))
# print(res)
print(q1)
# print(eval(q1.__repr__()))
q1 += q2
print(q1)

import math


class Quaternion2:

    def __init__(self, a, b=0, c=0, d=0):
        self.real = a
        self.i = b
        self.j = c
        self.k = d

    def __str__(self):
        return f'{self.real} + {self.i}i + {self.j}j + {self.k}k'

    def __repr__(self):
        return f'Quaternion({self.real}, {self.i}, {self.j}, {self.k})'

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Quaternion2(self.real + other, self.i, self.j, self.k)
        elif isinstance(other, Quaternion):
            a = self.real + other.real
            b = self.i + other.i
            c = self.j + other.j
            d = self.k + other.k
            return Quaternion2(a, b, c, d)
        else:
            raise TypeError('This type is not supported')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Quaternion(self.real * other, self.i * other,
                              self.j * other, self.k * other)
        elif isinstance(other, Quaternion2):
            a = (self.real * other.real - self.i * other.i -
                 self.j * other.j - self.k * self.k)
            b = (self.real * other.i + self.i * other.real +
                 self.j * other.k - self.k * other.j)
            c = (self.real * other.j + self.j * other.real +
                 self.k * other.i - self.i * other.k)
            d = (self.real * other.k + self.k * other.real +
                 self.j * other.j - self.j * other.i)
            return Quaternion2(a, b, c, d)
        else:
            raise ValueError('This type is not supported')

    def norm(self):
        return math.sqrt(
            self.real ** 2 + self.i ** 2 + self.j ** 2 + self.k ** 2)

    def convert(self):
        return Quaternion2(self.real, - self.i, -self.j, -self.k) / (
                self.norm() ** 2)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Quaternion(self.real / other, self.i / other,
                              self.j / other, self.k / other)
        elif isinstance(other, Quaternion):
            return self * other.convert()
        else:
            raise TypeError('This type is not supported')

    def __eq__(self, other):
        return all(
            [
                isinstance(self, Quaternion),
                isinstance(other, Quaternion),
                self.real == other.real,
                self.i == other.i,
                self.j == other.j,
                self.k == other.k,
            ]
        )
