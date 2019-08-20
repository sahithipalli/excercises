#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:51:35 2019

@author: sahithipydipalli
"""
#list less than 10
"""
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the 
list that are less than 5.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for b in a:
    if b <5 :
        print(b)
    else:
        pass
#    print(b)
    
"""
Extras:
1. Instead of printing the elements one by one, make a new list that 
has all the elements less than 5 from this list 
in it and print out this new list.
"""
print('extra1')
c=[]
for b in a:
    if b <5 :
        c.append(b)
    else:
        pass
print(c)
print(type(c))

"""
Extras:
2. Write this in one line of Python.

while a[]<5:
    c=c.append(a)
print(c) 
"""
print('extra2')
print([x for x in a if x <5])
"""
Extras
3. Ask the user for a number and return a list that contains only 
elements from the original list a that are smaller than that number 
given by the user.

"""
print('extra 3')
usr_num = int(input('enter a num'))
c=[]
for b in a:
    if b <usr_num :
        c.append(b)
    else:
        pass
print(c)
