#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:59:33 2017

@author: Tristan Dwyer

script to assign Kris Kringle gifts
inspiration came from https://www.youtube.com/watch?v=5kC5k5QBqcc

"""
import math
from random import shuffle
import numpy as np
import sympy as sy
import time


t0 = time.time()

list = [1,2,3,4,5,6,7,8,9,10,11,12]

def Derangement(x):
    shuffle(x)
    y = [x[-1]] + x[:-1]
    return x,y

def count(n):
    if n == 2 or n == 0:
        return 1
    elif n == 1:
        return 0
    elif  1 <= n <=20:
        return round(math.factorial(n) / math.e) # Computationally quick
    elif n.imag == 0 and n.real == int(n.real) and n > 0:
        return (n-1) * ( sy.subfact(n - 1) + sy.subfact(n - 2) ) # from http://mathworld.wolfram.com/Subfactorial.html
    else:
        raise ValueError()

print("The total number of possible derangements is: %f" % count(len(list)))
        
x,y = Derangement(list)

print(x,y)

for number in x:
    print("you are number: %f" % x[number-1])
    print("you are buying for: %f" % y[number-1])
    print("")
    
print("total run time = ", time.time()-t0)
# do this in groups for each family? Then pick from a different pile?
