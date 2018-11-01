import pandas as pd

df = pd.read_csv('PPP_01.02.2018.csv')
pd.__version__
'0.23.4'
type(df)

# Rename columns
df = df.rename(columns={'Currency': 'curr'})

# Filter data
condition = df['curr'] == 'Euro'

euro_df = df[condition]
euro_df = df[~condition]
column = pd.Series([i for i in range(19+1)])
df['data'] = column
df['data'][12]
df['data'][1:12]
df['data'][1:12:2]

# Drop duplicates
df = pd.concat([df, df, df])
df.loc[0]
df.iloc[0]
df.drop_duplicates(['curr'], keep='first', inplace=True)
# Equals
df = df.drop_duplicates(['curr'], keep='first')

# Group by
df = pd.concat([df, df, df])

grouped = df.groupby(['curr'])

count_data = grouped.count()

count_data = grouped.sum('data')

# Group by date
