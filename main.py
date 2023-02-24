class MergingFiles:
    """"""

    @staticmethod
    def create_merge_file(sorted_file_name, *args):
        """"""

        dict_name_and_numb = {}
        for file in args:
            with open(file, encoding='UTF-8') as f:
                dict_name_and_numb[file] = len(f.readlines())
        sort_files_dict = dict(sorted(dict_name_and_numb.items(), key=lambda i: i[1]))
        with open(sorted_file_name, 'w', encoding='UTF-8') as f_new:
            for name, numb in sort_files_dict.items():
                with open(name, encoding='UTF-8') as f:
                    data = f.read()
                    f_new.write(name + '\n')
                    f_new.write(str(numb) + '\n')
                    f_new.write(data + '\n')


def main():
    MergingFiles().create_merge_file('files/sorted.txt', 'files/1.txt', 'files/2.txt', 'files/3.txt')


if __name__ == '__main__':
    main()
