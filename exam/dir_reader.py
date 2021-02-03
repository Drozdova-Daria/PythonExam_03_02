import os


def check_file_name(file_name):
    count_of_symbol = dict.fromkeys(file_name, 0)
    for symbol in file_name:
        count_of_symbol[symbol] += 1
        if count_of_symbol[symbol] > 1:
            return True
    return False


class DirReader:
    def __init__(self, dir):
        self.walk = os.walk(dir)

    def work(self):
        for root, dirs, file_names in self.walk:
            for file_name in file_names:
                file, file_extention = os.path.splitext(file_name)
                if check_file_name(file):
                    file_path = root + "\\" + file_name
                    self.file_object = open(file_path)
                    yield self.file_object

    def __enter__(self):
        return self.work()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_object.close()

