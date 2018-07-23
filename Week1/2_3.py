# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:14:19 2018

@author: user
"""

import re

myString=input("Enter a string:")
print("Number of characters=",len(myString))
print("Digits=",len(re.findall(r'[0-9]',myString)))
print("Uppercase=",len(re.findall(r'[A-Z]',myString)))
print("Lowercase=",len(re.findall(r'[a-z]',myString)))
print("Adding \'ing\'",myString+"ing")

firstChar=myString[0]
myString=myString.replace(firstChar,'$')
myString=myString.replace('$',firstChar,1)
print("Modified string:"+myString)