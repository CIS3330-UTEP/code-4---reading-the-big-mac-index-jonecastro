import pandas as pd

filename = "big-mac-full-index.csv"

df = pd.read_csv(filename)

print(type(df['dollars']))

print(df)