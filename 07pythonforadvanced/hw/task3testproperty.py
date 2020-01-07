"""
Написать тесты(pytest or unittest) к предыдущим 2 заданиям, запустив которые, я бы смог бы проверить их корректность
Обязательно проверить всю критическую функциональность
"""
import time
import unittest
from task2 import Message


class TestMessage(unittest.TestCase):
    def test_set_concret_msg(self):
        m = Message()
        m.msg = 'concret msg'
        value = m.msg
        self.assertEqual(value, m.msg)
        print(1)

    def test_concret_msg_sleep_time_shorter_than__time_on_property(self):
        m = Message()
        m.msg = 'concret msg'
        value = m.msg
        time.sleep(1)
        self.assertEqual(value, m.msg)
        print(2)
    def test_concret_msg_sleep_time_longer_than__time_on_property(self):
        m = Message()
        m.msg = 'concret msg'
        value = m.msg
        time.sleep(6)
        self.assertNotEqual(value, m.msg)
        print(3)

    def test_rndm_msg_sleep_time_shorter_than_time_on_property(self):
        m = Message()
        value = m.msg
        time.sleep(1)
        self.assertEqual(value, m.msg)
        print(4)

    def test_rndm_msg_sleep_time_longer_than_time_on_property(self):
        m = Message()
        value = m.msg
        time.sleep(6)
        self.assertNotEqual(value, m.msg)
        print(5)

if __name__ == "__main__":
    unittest.main()