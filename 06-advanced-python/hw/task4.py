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


class PrintableFolder:
    """ Display all subfolders and relatives files.

    Class allowing to display all subfolders and
    files relative to the current directory.
    Additionally, it is possible to check if a file or folder
    exists in one of the directories or subdirectories"""

    def __init__(self, path, prefix):
        self.path = path
        self.prefix = prefix
        self.base_str = ''

    def __str__(self):
        self.base_str = self.base_str + '{}├── {}'.format(self.prefix, os.path.basename(self.path))
        for item in os.listdir(self.path):
            new_path = os.path.join(self.path, item)
            if os.path.isdir(new_path):
                print(PrintableFolder(new_path, self.prefix + '│ '))
            else:
                self.base_str = self.base_str + '\n{}│ ├── (file) {}'.format(self.prefix, item)
        return self.base_str

    def __contains__(self, item):
        self.dict = {os.path.basename(dirpath): filenames for dirpath, _, filenames in os.walk(os.getcwd())}

        for _, v in self.dict.items():
            if item in v:
                return True
            else:
                return False


path = os.getcwd()  # current work directory
prefix = ''
file = "task4.py"
test1 = PrintableFolder(path, prefix)
print(test1)
print(file in test1)


class PrintableFolder:
    """ Display all subfolders and relatives files.

    Class allowing to display all subfolders and
    files relative to the current directory.
    Additionally, it is possible to check if a file or folder
    exists in one of the directories or subdirectories"""

    def __init__(self):
        self.base_str = ''

    def __str__(self):
        return self.base_str

    def print_dir(self, path, prefix):
        self.base_str = self.base_str + '{}├── {}'.format(prefix, os.path.basename(path)) + "\n"

        for item in os.listdir(path):
            new_path = os.path.join(path, item)
            if os.path.isdir(new_path):
                self.print_dir(new_path, prefix + '│  ')
            else:
                self.base_str = self.base_str + '{}│  ├── (file) {}\n'.format(prefix, item)

    def __contains__(self, item):
        self.dict = {os.path.basename(dirpath): filenames for dirpath, _, filenames in os.walk(os.getcwd())}

        for _, v in self.dict.items():
            if item in v:
                return True
            else:
                return False


path = os.getcwd()  # current work directory
prefix = ''
file = "task4.py"
test1 = PrintableFolder()
test1.print_dir(path=path, prefix=prefix)
print(test1)
print(file in test1)
