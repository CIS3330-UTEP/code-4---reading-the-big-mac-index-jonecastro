import pandas as pd

df = pd.read.csv('big-mac-full-index.csv')

query = f"(iso_a3 =='NZL' or iso_a3 =='DNK')"

df_result = df.query(query)

Mean_dollar_price = df_result["dollar"].mean()

mean_dollar_price_two_decimals