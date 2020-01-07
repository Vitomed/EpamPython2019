"""
Написать тесты(pytest or unittest) к предыдущим 2 заданиям, запустив которые, я бы смог бы проверить их корректность
Обязательно проверить всю критическую функциональность
"""
import unittest
from task1 import SiamObj


class SiamMetaTest(unittest.TestCase):

    def test_equal(self):
        self.unit1 = SiamObj("1", 22, c=33)
        self.unit2 = SiamObj("1", 22, c=33)
        self.assertEqual(self.unit1, self.unit2)

    def test_not_equal(self):
        self.unit1 = SiamObj("1", 22, d=33)
        self.unit2 = SiamObj("1", d=33)
        self.unit3 = SiamObj(0, "11", p=15)
        self.assertNotEqual(self.unit1, self.unit3)
        self.assertNotEqual(self.unit1, self.unit2)

    def test_connec_method(self):
        self.unit1 = SiamObj(1, 2, q=12)
        self.unit2 = SiamObj(1, 2, z=4)
        self.unit3 = SiamObj(1, 2, z=4)
        self.unit1.connect(1, 2, z=4).z = 100
        self.assertEqual(self.unit2.z, 100)
        self.assertEqual(self.unit3.z, 100)

    def test_pool_method(self):
        self.unit2 = SiamObj(a=2)
        self.unit3 = SiamObj(a=3)
        pool = self.unit3.pool
        del self.unit3
        self.assertEqual(len(pool), 1)
