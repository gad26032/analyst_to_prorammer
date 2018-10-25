from lesson3.file_parser import txt_file_extractor

from lesson3 import file_parser

from lesson3.file_parser import DATA_DIR

'20180101 14:30'
'01-01-2018.'

# Запускать в Python Console

import pandas as pd

data_df = pd.read_csv('PPP_01.02.2018.csv')

data_df['Currency']

data_df['Currency'][0]

data_df['Currency'].unique()

for i in range(0, 10):
    pass


l = []
for i in range(0, 10 + 1, 2):
    l.append(i)

l = [i for i in range(0, 10 + 1)]




s = [i for i in range(19 + 1)]

ss = pd.Series(s)
data_df['my_data'] = ss

strings = [str(i) for i in range(19 + 1)]

str_series = pd.Series(strings)
data_df['strings'] = str_series

data_df['my_data_1'] = data_df['my_data'].apply(float)
data_df['my_data'] == data_df['my_data_1']

lambda x: x + 2

def parse(x, y):
    print(y)
    result = x.split('-')[-1]
    return result



ADD = 5

data_df['result_1'] = data_df['Gillette Fusion ProGlide razor'].apply(parse)

data_df['my_data_add'] = data_df['my_data'].apply(lambda x: x + 2)


super_parse = parse()

super_parse('sdfsdf')

