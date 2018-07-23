# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:36:25 2018

@author: user
"""

x=input("Enter string:")
x=x[len(x)-1]+x[1:len(x)-1]+x[0]
print(x)