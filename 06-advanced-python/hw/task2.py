"""
Реализовать класс Quaternion, позволяющий работать с кватернионами
https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD
Функциональность (магическими методами):
- сложение +
- умножение
- деление
- сравнение
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
        if isinstance(other, int) or isinstance(other, float):
            new_a = self.a + other
            new_b = self.b
            new_c = self.c
            new_d = self.d

        elif isinstance(other, Quaternion):
            new_a = self.a + other.a
            new_b = self.b + other.b
            new_c = self.c + other.c
            new_d = self.d + other.d

        else:
            raise TypeError("Undefined tcpe")
        return Quaternion(new_a, new_b, new_c, new_d)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.a += other

        elif isinstance(other, Quaternion):
            self.a += other.a
            self.b += other.b
            self.c += other.c
            self.d += other.d

        else:
            raise TypeError("Undefined type")

    def __sub__(self, other):  # вычитание
        if isinstance(other, int) or isinstance(other, float):
            new_a = self.a - other
            new_b = self.b
            new_c = self.c
            new_d = self.d

        elif isinstance(other, Quaternion):
            new_a = self.a - other.a
            new_b = self.b - other.b
            new_c = self.c - other.c
            new_d = self.d - other.d
        else:
            raise TypeError("Undefined tcpe")
        return Quaternion(new_a, new_b, new_c, new_d)

    def __rsub__(self, other):

        if isinstance(other, int) or isinstance(other, float):
            new_a = other - self.a
            new_b = -self.b
            new_c = -self.c
            new_d = -self.d

        elif isinstance(other, Quaternion):
            self.__sub__(other)
        else:
            raise TypeError("Undefined type")
        return Quaternion(new_a, new_b, new_c, new_d)

    def __isub__(self, other):
        if isinstance(other, Quaternion):
            self.a -= other.a
            self.b -= other.b
            self.c -= other.c
            self.d -= other.d

        elif isinstance(other, (int, float)):
            self.a -= other
        else:
            raise TypeError('Undefined object')
        return self

    def __mul__(self, other):  # умножение
        if isinstance(other, int) or isinstance(other, float):
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
        if isinstance(other, int) or isinstance(other, float):
            self.a *= other
            self.b *= other
            self.c *= other
            self.d *= other

        elif isinstance(other, Quaternion):

            new_a = (self.a * other.a - self.b * other.b -
                     self.c * other.c - self.d * other.d)

            new_b = (self.a * other.b + self.b * other.a +
                     self.c * other.d - self.d * other.c)

            new_c = (self.a * other.c - self.b * other.d +
                     self.c * other.a - self.d * other.b)

            new_d = (self.a * other.d + self.b * other.c -
                     self.c * other.b + self.d * other.a)
        else:
            raise TypeError("Undefined obj")
        return Quaternion(new_a, new_b, new_c, new_d)

    def __truediv__(self, other):  # деление
        if isinstance(other, int) or isinstance(other, float):
            new_a = self.a / other
            new_b = self.b / other
            new_c = self.c / other
            new_d = self.d / other

        elif isinstance(other, Quaternion):

            devider = (self.a + self.a + self.b + self.b +
                       self.c + self.c + self.d + self.d)

            new_a = (-self.a * other.b + self.b * other.a -
                     self.c * other.d + self.d * other.c) / devider

            new_b = (self.a * other.b + self.b * other.c +
                     self.c * other.a - self.d * other.a) / devider

            new_c = (-self.a * other.c + self.b * other.d +
                     self.c * other.a - self.d * other.b) / devider

            new_d = (-self.a * other.d - self.b * other.c +
                     self.c * other.b + self.d * other.a) / devider
        else:
            raise TypeError("Undefined type")
        return Quaternion(new_a, new_b, new_c, new_d)

    def __gt__(self, other):
        if isinstance(other, Quaternion):
            return self.a > other.a or self.b > other.b or self.c > other.c or self.d > other.b
        else:
            raise TypeError(f"'>' not supported between instances of Quaternion and {type(other)}")

    def __lt__(self, other):
        if isinstance(other, Quaternion):
            return self.a < other.a or self.b < other.b or self.c < other.c or self.d < other.b
        else:
            raise TypeError(f"'<' not supported between instances of Quaternion and {type(other)}")

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


def test_add(q1, q2):
    assert q1 + q2 == Quaternion(q1.a + q2.a, q1.b + q2.b, q1.c + q2.c, q1.d + q2.d)
    for s in [-3, -2.3, -1.2, -1.0, 0.0, 0, 1.0, 1, 1.2, 2.3, 3]:
        assert (q1 + s == Quaternion(q1.a + s, q1.b, q1.c, q1.d))
        assert (s + q1 == Quaternion(q1.a + s, q1.b, q1.c, q1.d))


def test_subtract(q1, q2):
    assert q1 - q2 == Quaternion(q1.a - q2.a, q1.b - q2.b, q1.c - q2.c, q1.d - q2.d)
    for s in [-3, -2.3, -1.2, -1.0, 0.0, 0, 1.0, 1, 1.2, 2.3, 3]:
        assert (q1 - s == Quaternion(q1.a - s, q1.b, q1.c, q1.d))
        assert (s - q1 == Quaternion(s - q1.a, -q1.b, -q1.c, -q1.d))

def test_divide(q):
    assert q / 1.0 == q
    assert q / 1 == q
    for s in [-2.3, -1.2, -1.0, 1.0, 1, 1.2, 2.3]:
        assert q / s == q * (1.0 / s)

def test_mul(q):
    assert q * 1.0 == q
    assert q * 1 == q
    assert 1.0 * q == q
    assert 1 * q == q
    assert 0.0 * q == q * 0.0
    for s in [-3, -2.3, -1.2, -1.0, 0.0, 0, 1.0, 1, 1.2, 2.3, 3]:
        assert q * s == Quaternion(s * q.a, s * q.b, s * q.c, s * q.d)
        assert s * q == q * s





if __name__ == '__main__':
    q1 = Quaternion(10, 2, 7, 1)
    q2 = Quaternion(0, 22, 3, 4)
    test_add(q1, q2)
    test_subtract(q1, q2)
    test_mul(q2)
    test_divide(q1)
    print(q1 < q2)

