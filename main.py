class Files:
    """"""

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.numb_rows = self.__get_numb_rows()
        self.data = self.__get_data_file()

    def __get_data_file(self):
        with open(self.file_name, encoding='UTF-8') as f:
            self.data = f.read()
        return self.data

    def __get_numb_rows(self):
        with open(self.file_name, encoding='UTF-8') as f:
            self.numb_rows = len(f.readlines())
        return self.numb_rows

    def __lt__(self, other):
        if not isinstance(other, Files):
            return "Not a Files!"
        return self.numb_rows < other.numb_rows

    def __gt__(self, other):
        if not isinstance(other, Files):
            return "Not a Files!"
        return self.numb_rows > other.numb_rows

    def __eq__(self, other):
        if not isinstance(other, Files):
            return "Not a Files!"
        return self.numb_rows == other.numb_rows


def create_dict_files(list_file: list):
    """"""

    dict_files = {}
    for file in list_file:
        if not isinstance(file, Files):
            return print('Список "list_files" должен состоять из элементов класса "Files".')

    for file in list_file:
        attr_files = {}
        attr_files['numb_rows'] = file.numb_rows
        attr_files['data'] = file.data
        dict_files[file.file_name] = attr_files

    return dict_files


def create_sorted_file(new_file_name, dict_file: dict):
    """"""

    with open(new_file_name, 'w', encoding='UTf-8') as f:
        for key, value in dict_file.items():
            f.write(key + '\n')
            f.write(str(value['numb_rows']) + '\n')
            f.write(value['data'] + '\n')


def main():
    file_1 = Files('files/1.txt')
    file_2 = Files('files/2.txt')
    file_3 = Files('files/3.txt')
    dict_files = create_dict_files(sorted([file_1, file_2, file_3]))
    create_sorted_file('files/sorted.txt', dict_files)


if __name__ == '__main__':
    main()
