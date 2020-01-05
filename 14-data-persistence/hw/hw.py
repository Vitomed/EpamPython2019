import json
import pickle
import redis
import sqlite3
# import pymongo

class Saver:

    def __init__(self, obj, protocol, storage):
        self.obj_ref = obj
        self.protocol = protocol
        self.storage = storage

    def serialize(self):
        pass

    def deserialize(self):
        pass


class Receiver:

    def __init__(self, obj, protocol, storage):
        self.obj_ref = obj
        self.protocol = protocol
        self.storage = storage

    def serialize(self):
        pass

    def deserialize(self):
        pass


def save(obj_ref, protocol, storage):
    print("1", obj_ref)
    print("2", protocol)
    print("3", storage)
    pass

def receive(obj_ref, protocol, storage):
    pass

# data = {
#     'a': [1, 2.0, 3, 4+6j],
#     'b': ("character string", b"byte string"),
#     'c': {None, True, False}
# }
#
# with open('data.pickle', 'wb') as f:
#     # Pickle the 'data' dictionary using the highest protocol available.
#     pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
#
#
# with open('data.pickle', 'rb') as f:
#     # The protocol version used is detected automatically, so we do not
#     # have to specify it.
#     data = pickle.load(f)
# print(data)


def serialization_picle(filename, object):
    name = filename + ".pickle"
    with open(name, "wb") as file:
        pickle.dump(object, file, 2)


def deserialization_picle(filename):
    name = filename + ".pickle"
    with open(name, "rb") as file:
        data = pickle.load(file)
        return data


def serialization_json(filename, object):
    name = filename + ".json"
    with open(name, "w") as file:
        json.dump(object, file)


def deserialization_json(filename):
    name = filename + ".json"
    with open(name, "r") as file:
        data = json.load(file)
        return data



def redis_handler(data, status):
    r = redis.Redis()
    if status == 1:
        r.set(hash(data), data)
        hashes.append(hash(data))
    else:
        return r.get(data)

# def mongo_handler(data, status):
#     client = pymongo.MongoClient(host='localhost', port=27017)
#     if status == 1:
#         db = client['test_db']
#         coll = db['test_coll']
#         hash_ = coll.insert({'data': data})
#         hashes.append(hash_)
#     else:
#         db = client['test_db']
#         coll = db['test_coll']
#         res = coll.find_one(data)
#         return coll.find_one(res)['data']

def deserialize_json(data):
    return json.loads(data)


def deserialize_pickle(data):
    return pickle.loads(data)


def serialize_json(data):
    return json.dumps(data)


def serialize_pickle(data):
    return pickle.dumps(data)


def set(data, protocol, storage):
    if protocol == 'json':
        data = serialize_json(data)
    elif protocol == 'pickle':
        data = serialize_pickle(data)
    storage_links[storage](data, 1)


def get(data, protocol, storage):
    result = storage_links[storage](data, 2)
    if protocol == 'json':
        return deserialize_json(result)
    elif protocol == 'pickle':
        return deserialize_pickle(result)


# storage_links = {'redis': redis_handler, 'mongo': mongo_handler}
# storage_links = {'redis': redis_handler}
# hashes = []

# if __name__ == '__main__':
    # data_ = {"name": "Scott", "website": "stackabuse.com", "from": "Nebraska"}
    # set(data_, 'json', 'redis')
    # result = get(hashes[0], 'json', 'redis')
    # print(result)
    # set(data_, 'json', 'mongo')
    # result = get(hashes[1], 'json', 'mongo')
    # print(result)

# =====================================================

r = redis.Redis()

restaurant_484272 = {
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

from pprint import pprint

# r.set(484272, json.dumps(restaurant_484272)) # True
# # pprint(json.loads(r.get(484272)))
# obj = json.loads(r.get(484272))
# # obj = pprint(json.loads(r.get(484272)))
# pprint(obj)


# r.set(484273, pickle.dumps(restaurant_484272)) # True
# # pprint(json.loads(r.get(484272)))
# obj = pickle.loads(r.get(484273))
# # obj = pprint(json.loads(r.get(484272)))
# pprint(obj)

# print(hash(restaurant_484272))
hash_list = list()
hash_list.append(abs(hash(str(restaurant_484272))))

r.set(hash_list[0], json.dumps(restaurant_484272)) # True
# pprint(json.loads(r.get(484272)))
obj = json.loads(r.get(hash_list[0]))
# obj = pprint(json.loads(r.get(484272)))
# pprint(obj)

# =====================================================

import os

print(os.environ["REDIS_ENDPOINT"])