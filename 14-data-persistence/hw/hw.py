import json
import pickle
import redis
from pprint import pprint


class JsonSerializer:

    @staticmethod
    def serialize(data):

        try:
            serialize_data = json.dumps(data)
        except TypeError:
            raise TypeError(f"Object of type {type(data)} is not JSON serializable")
        else:
            print("json serialization")
            return serialize_data

    @staticmethod
    def deserialize(new_data):
        if new_data is not None:
            deserialize_data = json.loads(new_data)
            print("json deserialization")
            return deserialize_data


class PickleSerializer:

    @staticmethod
    def serialize(data):
        try:
            serialize_data = pickle.dumps(data)
        except TypeError:
            raise TypeError(f"Object of type {type(data)} is not PICKLE serializable")
        else:
            print("pickle serialization")
            return serialize_data

    @staticmethod
    def deserialize(new_data):
        if new_data is not None:
            deserialize_data = pickle.loads(new_data)
            print("pickle deserialization")
            return deserialize_data


class MetaSingetonRedis(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class RedisHandler(metaclass=MetaSingetonRedis):

    def __init__(self, protocol):
        self.r = redis.Redis(host="localhost", port=6379)
        self.protocol = protocol

    def store_data(self, serial_data, key):
        print("redis")
        self.r.set(key, serial_data)

    def recive_data(self, key):
        return self.r.get(key)


class FileHandler:

    def __init__(self, proto):
        self.name = "file"
        self.protocol = proto
        print("file")

    def store_data(self, serial_data, key):
        operation_mode = "wb" if self.protocol == "pickle" else "w"
        with open(f"{key}.txt", operation_mode) as write_file:
            write_file.write(serial_data)

    def recive_data(self, key):
        operation_mode = "rb" if self.protocol == "pickle" else "r"
        with open(f"{key}.txt", operation_mode) as read_file:
            data = read_file.read()
            return data


protocols = {"json": JsonSerializer, "pickle": PickleSerializer}
storage_type = {"redis": RedisHandler, "file": FileHandler}

def worker_saver(data, name_serialize, storage_name):
    key = [key for key in data.keys()][0]

    protocol = protocols[name_serialize]
    storage = storage_type[storage_name]

    inst_protocol = protocol()
    ser_obj = inst_protocol.serialize(data)

    inst_storage = storage(name_serialize)
    inst_storage.store_data(ser_obj, key)


def worker_reciver(data, name_serialize, storage_name):
    key = [key for key in data.keys()][0]

    protocol = protocols[name_serialize]
    storage = storage_type[storage_name]

    inst_protocol = protocol()
    inst_storage = storage(name_serialize)

    ser_obj = inst_storage.recive_data(key)
    deser_obj = inst_protocol.deserialize(ser_obj)

    pprint(deser_obj)

if __name__ == "__main__":

    key_name = "my_key"
    obj = {
        "name": "Ravagh",
        "type": "Persian",
        "address": {
            "street": {
                "line1": "11 E 30th St",
                "line2": "APT 1",
            },
            "city": "New York",
            "state": "NY",
            "zip": 10016,
        }
    }

    data = {key_name: obj}

    print("="*30)
    worker_saver(data, "json", "redis")
    worker_reciver(data, "json", "redis")


    print("="*30)
    worker_saver(data, "json", "file")
    worker_reciver(data, "json", "file")

    print("="*30)
    worker_saver(data, "pickle", "redis")
    worker_reciver(data, "pickle", "redis")


    print("="*30)
    worker_saver(data, "pickle", "file")
    worker_reciver(data, "pickle", "file")