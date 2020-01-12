"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):

    setattr(cls, "counter", 0)
    obj_init = cls.__init__

    def __init__(self, *args, **kwargs):
        cls.counter += 1
        obj_init(self, *args, **kwargs)

    def get_created_instances(self=None):
        return cls.counter

    def reset_instances_counter(self=None):
        count_now = cls.counter
        cls.counter = 0
        return count_now

    setattr(cls, "__init__", __init__)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)

    return cls


@instances_counter
class User:
    def __init__(self, a):
        self._a = a

    @property
    def a(self):
        return self._a + 10


if __name__ == '__main__':
    assert User.get_created_instances() == 0
    user, _, _ = User(2), User(2), User(2)
    assert user.get_created_instances() == 3
    assert user.get_created_instances() == 3
    assert user.reset_instances_counter() == 3
    assert user.get_created_instances() == 0
    assert user.a == 12


