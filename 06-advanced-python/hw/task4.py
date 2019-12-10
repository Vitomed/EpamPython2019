"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:

> print(folder1)

V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1

А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True

"""
import os.path


# class PrintableFolder:
#     def __init__(self, name, content):
#         self.name = name
#         self.content = content
#
#     def __str__(self):
#         pass


class PrintableFile:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def __contains__(self, item):
        content = {}
        curr_dir = os.getcwd()
        for (dirpath, dirnames, filenames) in os.walk(curr_dir):
            name_of_dir = os.path.basename(dirpath)
            content.update({name_of_dir: filenames})

        all_folders = list(content.values())
        for curr_folder in range(len(all_folders)):
            if item in all_folders[curr_folder]:
                return True
        return False

"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
###################################################


# base_str = ''
def print_dir(path, prefix=''):
    base_str = ""
    # global base_str
    # print('{}├── {}'.format(prefix, os.path.basename(path)))
    base_str = base_str + '{}├── {}'.format(prefix, os.path.basename(path)) + "\n"

    for item in os.listdir(path):
        p = os.path.join(path, item)
        if os.path.isdir(p):
            print_dir(p, prefix + '│  ')
        else:
            base_str = base_str + '{}│  ├── (file) {}\n'.format(prefix, item)
    return base_str


# print_dir(os.getcwd())
# print(print_dir(os.getcwd()))


class PrintableFolder:
    def __init__(self, path, prefix, base_dir=None):
        # self.name = name
        # self.content = content
        self.path = path
        self.prefix = prefix
        self.base_str = ''
        self.index = 0

    def __str__(self):
        self.base_str = self.base_str + '{}├── {}'.format(self.prefix, os.path.basename(self.path))
        for item in os.listdir(self.path):
            p = os.path.join(self.path, item)
            if os.path.isdir(p):
                print(PrintableFolder(p, self.prefix + '│ '))
            else:
                self.base_str = self.base_str + '\n{}│ ├── (file) {}'.format(self.prefix, item)
        return self.base_str


# path = os.getcwd()
# prefix = ''
# test1 = PrintableFolder(path,prefix)
# print(test1)



class PrintableFolder:

    current_dir = os.getcwd()

    def __init__(self, path, prefix):
        # self.name = name
        # self.content = content
        self.path = path
        self.prefix = prefix
        self.base_str = ''

    def __str__(self):
        self.print_dir(self.path, self.prefix)
        return self.base_str

    def print_dir(self, path, prefix):
        self.base_str = self.base_str + '{}├── {}'.format(prefix, os.path.basename(path)) + "\n"
        for item in os.listdir(path):
            p = os.path.join(path, item)
            if os.path.isdir(p):
                self.print_dir(p, prefix + '│  ')
            else:
                self.base_str = self.base_str + '{}│  ├── (file) {}\n'.format(prefix, item)


path = os.getcwd()
prefix = ''
test1 = PrintableFolder(path, prefix)
print(test1)
check_file = PrintableFile()
file = "task4.py"
print(file in check_file)