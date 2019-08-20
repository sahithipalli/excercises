# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import time
from datetime import date
#from datetime import datetime
#from datetime import timedelta
#import time
#import date


# this is a demo #
print("Its my first python")

# input age o/p which year he turns 100

name = input('Whats your name :')
print('your name is :' +name)
age = input('Whats your age :')

print('your age is :' +age)
today= date.today()
print(today)
tommorrow = today.year
print(tommorrow)
type(tommorrow)
day_mth_yr = today.strftime("%d/%m/%Y")
print('Day month year : '+day_mth_yr)
year = today.strftime("%Y")
print('Current Year : '+ year)
year= int(year)
age= int(age)
print('Current Year in int: ', year)
print('Current age in int: ', age)
hundredth_year = tommorrow +(100-age)
print('Current age in hundredth_year: ', hundredth_year)
#+year
#yr_100 = sysdate
