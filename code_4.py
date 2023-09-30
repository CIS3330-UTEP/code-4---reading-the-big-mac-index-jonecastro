import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)


def get_big_mac_price_by_year(year, country_code):
    country_code = country_code.upper()
    df_by_date = df[df['date'].str.startswith(str(year)) & (df["iso_a3"] == country_code)]
    mean_dollar_price = round(df_by_date['dollar_price'].mean(), 2)
    return mean_dollar_price

def get_big_mac_by_country(country_code):
    country_code = country_code.upper()
    df_by_country = df[df['iso_a3'] == country_code]
    return round(df_by_country['dollar_price'].mean(), 2)

def get_the_cheapest_big_mac_price_by_year(year):
    new_query = f"(date >= '{year}-01-01' & date <= '{year}-12-31')"
    df_by_year = df.query(new_query)
    index_of_min_value = df_by_year['dollar_price'].idxmin()
    cheapest_burger = df_by_year.loc[index_of_min_value]
    result = f"{cheapest_burger['name']}({cheapest_burger['iso_a3']}), ${round(cheapest_burger['dollar_price'], 2)}"
    return result


def get_the_most_expensive_big_mac_price_by_year(year):
    new_query = f"(date >= '{year}-01-01' & date <= '{year}-12-31')"
    df_by_year = df.query(new_query)
    index_of_max_value = df_by_year['dollar_price'].idxmax()
    expensive_burger = df_by_year.loc[index_of_max_value]
    result = f"{expensive_burger['name']}({expensive_burger['iso_a3']}), ${round(expensive_burger['dollar_price'], 2)}"
    return result

if __name__ == "__main__":
    year = '2000'
    country_code = 'mex'

    print("Average Big Mac price by year and country:", get_big_mac_price_by_year(year, country_code))
    print("Average Big Mac price by country:", get_big_mac_by_country(country_code))
    print("Cheapest Big Mac price by year:", get_the_cheapest_big_mac_price_by_year(year))
    print("Most Expensive Big Mac price by year:", get_the_most_expensive_big_mac_price_by_year(year))
    