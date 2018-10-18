import os
import glob

DATA_DIR = './lesson3/test_data/filings'

# list dir

# Посмотреть содержимое папки
#   проверить содержимое
#      либо папка либо файл
#             если папка то идем внутрь
#             если файл проверяем .txt или нет
#                 если .txt то сохраняем путь до файла
#                 если нет то ничего не делаем

list_data = os.listdir(DATA_DIR)


def txt_file_extractor():
    result = []

    for item in list_data:
        current_path = DATA_DIR + '/' + item
        tmp_list_data = os.listdir(current_path)
        for sub_item in tmp_list_data:
            sub_path = current_path + '/' + sub_item
            sub_file_list = os.listdir(sub_path)
            for txt_file in sub_file_list:
                txt_path = sub_path + '/' + txt_file
                result.append(txt_path)
    return result


rr = txt_file_extractor()


g = glob.glob(os.path.join(DATA_DIR, '*/*/*.txt'))

for i in g:
    print(i)
# find txt

# find files using glob
