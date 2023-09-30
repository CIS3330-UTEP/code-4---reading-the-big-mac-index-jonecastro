import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

index_of_min_value = df['dollar_price'].idxmin()

print(index_of_min_value)

print(index_of_min_value)

print(df.loc[index_of_min_value])

print(df['dollar_price'].min())