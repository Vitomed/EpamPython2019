"""
Написать свое property c кэшем и таймаутом
полностью повторяет поведение стандартной property за исключением:
    * хранит результат работы метода некоторое время, которое передается
      параметром в инициализацию проперти
    * пересчитывает значение, если таймер истек
"""


import time
import uuid


def timer_property(t:int):

    class TimerProperty:

        def __init__(self, fget=None, fset=None, fdel=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            self.time = 0
            self.value = None

        def __get__(self, obj, objtype=None):

            if obj is None:
                return self

            if self.fget is None:
                raise AttributeError("unreadable attr")

            if time.time() - self.time > t:
                self.time = time.time()
                self.value = self.fget(obj)

                return self.value  # return new value (time is over)

            return self.value  # return old value (time is not over)

        def __set__(self, obj, value):

            if self.fset is None:
                raise AttributeError("can't set attr")
            self.time = 0
            self.fset(obj, value)
            # self.value = value

        def __delete__(self, obj):
            if self.fdel is None:
                raise AttributeError("can't delete attr")
            self.fdel(obj)

        def getter(self, fget):
            """To call a getter you need to add it to our property

            return type(self) - a new instance of the property
            fget - new, fset and fdel - remained unchanged"""

            return type(self)(fget, self.fset, self.fdel)

        def setter(self, fset):
            """To call a setter you need to add it to our property

            return type(self) - a new instance of the property
            fset - new, fget and fdelet - remained unchanged"""

            return type(self)(self.fget, fset, self.fdel)

        def deleter(self, fdel):
            """To call a del you need to add it to our property

            return type(self) - a new instance of the property
            fdel - new, fget and fset - remained unchanged"""

            return type(self)(self.fget, self.fset, fdel)

    return TimerProperty


def get_message():
    """
    Return random string
    """
    return uuid.uuid4()


class Message:

    @timer_property(t=3)
    def msg(self):
        self._msg = get_message()
        return self._msg

    @msg.setter # reset timer also
    def msg(self, param):
        self._msg = param


if __name__ == '__main__':
    # m = Message()
    # initial = m.msg
    # assert initial is m.msg
    # time.sleep(3)
    # assert initial is m.msg
    # time.sleep(3)
    # assert initial is not m.msg
    m = Message()
    m.msg = 'hello'
    print(m.msg)
    initial = m.msg
    print(initial is m.msg)
    time.sleep(6)
    print(initial is m.msg)
