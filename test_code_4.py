import os,sys
import random
import pytest
from code_4 import get_big_mac_price_by_year
from code_4 import get_big_mac_price_by_country
from code_4 import get_the_cheapest_big_mac_price_by_year
from code_4 import get_the_most_expensive_big_mac_price_by_year

def check_if_file_exists():
    try:
        exists = os.path.exists("code_4.py")
        assert exists == True
    except:
        sys.exit()

def test_big_mac_price_by_year():
    country_code = ['arg','usa','mex','arg','kor','jpn','gbr','bra','chn','can']
    year = [2012,2018,2009,2017,2019,2012,2014,2008,2016,2006]
    value = [4.4, 4.62, 2.39, 3.8, 3.92, 4.13, 4.78, 4.73, 2.73, 3.07]
    check_if_file_exists()
    random_choice = random.randint(1,10)
    assert get_big_mac_price_by_year(year[random_choice-1],country_code[random_choice-1]) == value[random_choice-1]

def test_big_mac_price_by_country():
    country_code = ['arg','rus','mex','twn','kor','jpn','gbr','zaf','chn','hun']
    value = [3.04, 1.98, 2.68, 2.37, 3.35, 3.14, 3.98, 2.13, 2.37, 3.06]
    check_if_file_exists()
    random_choice = random.randint(1,10)
    assert get_big_mac_price_by_country(country_code[random_choice-1])  == value[random_choice-1]

def test_the_cheapest_big_mac_price_by_year():
    year = [2008,2012,2019,2016,2011,2000,2004,2007,2015,2005]
    value =['Malaysia(MYS): $1.7', 'India(IND): $1.58', 'Russia(RUS): $1.65', 'Venezuela(VEN): $0.66', 'India(IND): $1.89', 'Malaysia(MYS): $1.19', 'Saudi Arabia(SAU): $0.64', 'China(CHN): $1.41', 'Venezuela(VEN): $0.67', 'China(CHN): $1.27']
    check_if_file_exists()
    random_choice = random.randint(1,10)
    assert get_the_cheapest_big_mac_price_by_year(year[random_choice-1]) == value[random_choice-1]

def test_the_most_expensive_big_mac_price_by_year():
    year = [2003,2014,2016,2014,2013,2005,2006,2010,2011,2009]
    value = ['Switzerland(CHE): $4.6', 'Norway(NOR): $7.8', 'Switzerland(CHE): $6.59', 'Norway(NOR): $7.8', 'Venezuela(VEN): $9.08', 'Norway(NOR): $6.06', 'Norway(NOR): $7.05', 'Norway(NOR): $7.2', 'Norway(NOR): $8.31', 'Norway(NOR): $6.15']
    check_if_file_exists()
    random_choice = random.randint(1,10)
    assert get_the_most_expensive_big_mac_price_by_year(year[random_choice-1]) == value[random_choice-1]

