import os
import hashlib


def get_hash_file(file):
    print("get", file)
    with open(file, "rb") as file:
        hash_value = file.read()
        return hashlib.sha256(hash_value).hexdigest()


def main(path, test_hash_value):
    if not os.path.exists(path):
        return -1
    print(path)
    try:
        for root, dirs, files in os.walk(path):
            print("r", root)
            print("d", dirs)
            print("f", files)
            for filename in files:
                print("files", filename)
                if os.path.isfile(os.path.join(root, filename)):
                    print("is file", os.path.join(root, filename))
                    path_to_file = os.path.join(root, filename)
                    print("hash f", get_hash_file(path_to_file))
                    hash_file_value = get_hash_file(path_to_file)
                    if hash_file_value == test_hash_value:
                        print("True", os.path.abspath(root))

    except Exception as e:
        print("Exc", e)


if __name__ == "__main__":
    my_path = "/home/vitomed/PycharmProjects/WinterEpamPython2019/11-programming-and-debugging"
    # print("path", os.path.abspath(my_path))

    main(my_path, 12)