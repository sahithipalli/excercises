#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 08:35:38 2019

@author: sahithipydipalli
"""

#even or odd

num = int(input('print a number to check if it is even or odd'))
print(num)
if num%4==0:
    print('multiple of 4')
elif num%2 ==0:
        print('even')
else:
    print('odd')

num_usr = int(input('enter a num to chk'))
num_chk = int(input('enter num to chk with'))
if num_usr % num_chk == 0:
        print('divisible')
else:
    print('not divisible')
    
            