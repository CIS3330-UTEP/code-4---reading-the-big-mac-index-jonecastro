## CIS3330-Reading-The-Big-Mac-Index

## Instructions

In this coding assignment, you are asked to create a little program to find information in a CSV file. You can code your program using the libraries CSV or Pandas.
Your program should include the following functions:

* `get_big_mac_price_by_year`
  + The function receives the **year** and the **country_code in lower case**
  + The function should return **mean value** in the **specific year** of the big mac in dollars ('dollar_pice' column)
  + The value must be rounded to **2** decimal numbers
* `get_big_mac_price_by_country`
  + The function receives the **country_code in lower case**
  + The function should return **mean value** of the big mac in dollars ('dollar_pice' column)
  + The value must be rounded to **2** decimal numbers
* `get_the_cheapest_big_mac_price_by_year`
  + The function receives the **year** 
  + The function should return the following output from the place that has the cheapest big mac: "country_name(country_code): $dollar_price" (replace the appropriate values)
  + For example, the output for 2008 will be: **'Malaysia(MYS): $1.7'**
* `get_the_most_expensive_big_mac_price_by_year`
  + The function receives the **year** 
  + The function should return the following output from the place that has the most expensive big mac: "country_name(country_code): $dollar_price" (replace the appropriate values)
  + For example, the output for 2003 will be: **'Switzerland(CHE): $4.6'**

## Important notes

* The country_code is stored under the column **'iso_a3'**
* For the functions `get_big_mac_price_by_year`and `get_big_mac_price_by_country` you must return a float rounded to **2** decimal spaces.
* For the functions `get_the_cheapest_big_mac_price_by_year` and `get_the_most_expensive_big_mac_price_by_year`, you must return a message with exactly the same format.
* You need to program your interface under the if statement: `if __name__ == "__main__":`.
* It is recommended to use Pandas, but you are free to use the CSV module.
* Use the built-in function round() to round decimal numbers. For example: `round(0.5556,2)` should return **0.56**

## Copyright disclosure

* The file `big-mac-full-index` was obtained from [https://github.com/TheEconomist/big-mac-data] (https://github.com/TheEconomist/big-mac-data). The file is protected under the MIT License [https://github.com/TheEconomist/big-mac-data/blob/master/LICENCE](https://github.com/TheEconomist/big-mac-data/blob/master/LICENCE).