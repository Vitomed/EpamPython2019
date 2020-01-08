import os
import hashlib
import chardet
import cProfile


def get_hash_file(file):
    with open(file, "rb") as file:
        hash_value = file.read()
    return hashlib.sha256(hash_value).hexdigest()


def walker_path(path, searching_hash):
    if not os.path.exists(path):
        return -1
    try:
        for root, dirs, files in os.walk(path):
            for filename in files:
                path_to_file_ = os.path.join(root, filename)
                hash_file_value = get_hash_file(path_to_file_)
                if hash_file_value == searching_hash:
                    return os.path.abspath(path_to_file_)

    except Exception as e:
        print("Exc", e)


def main(path, searching_hash):
    path_to_file = walker_path(path, searching_hash)

    if path_to_file:
        print("1",path_to_file)
        with open(path_to_file, "rb") as file: print(chardet.detect(file.read()))
    else:
        print("File not found")


if __name__ == "__main__":
    p = "/home/vitomed/PycharmProjects/WinterEpamPython2019/"
    s = "37f7cc05f119a614876a98753db519ded14956d2169dbb05c4c89baf45e25c8a"
    cProfile.run("main(p,s)")
    # main(p, s)