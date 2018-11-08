import pandas as pd
import matplotlib
DATA_URL = 'https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1538654315&period2=1541332715&interval=1d&events=history&crumb=nMbdNPrWibC'


df = pd.read_csv('lesson6/AAPL.csv')

describe_df = df.describe()
describe_df.reset_index(inplace=True)



def autocorr(path_to_file):
    df = pd.read_csv(path_to_file)

    for col in df.columns:
        if col == 'Date':
            pass
        else:
            print(col, ':', df[col].autocorr(2))


d = '2018-10-10'
date = pd.to_datetime(d)

df['Date'] = df['Date'].apply(pd.to_datetime)






