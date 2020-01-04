import json
import pickle


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

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('data.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


with open('data.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)
print(data)


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




















