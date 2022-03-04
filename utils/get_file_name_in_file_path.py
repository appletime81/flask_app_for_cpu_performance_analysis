from tokenize import String


def get_test_info_from_file_name(fileName: String):
    file_name_split_list = fileName.split('/')
    print(file_name_split_list)
    print(file_name_split_list[-1])
    pass

if __name__ == '__main__':
    get_test_info_from_file_name('2-4-32.txt')