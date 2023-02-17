# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:53:09 2023

@author: romina
"""

number1 = '2.5'
number2 = '2'

"""
use float() to turn string into float number
"""

result = float(number1) / float(number2)
print(result)   

print(int(result))  # use int() to get the integer part of the result

remainder =  float(number1) % float(number2)