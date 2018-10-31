#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 22:51:25 2018

@author: miteshjoshi
"""
import collections
num_shoes=int(input("Enter Number of Shoes available:\n"))
num_cust=int(input("Enter Number of Customers:\n"))
shoe_sizes=collections.Counter(map(int,input("Enter the sizes available:\n").split()))
print(num_shoes,num_cust,shoe_sizes)
total=0
for i in range(num_cust):
    size, price = map(int,input("Enter Size and Price:\n").split())
    if shoe_sizes[size]:
        total=total+price
        shoe_sizes[size]= shoe_sizes[size] -1
        print(shoe_sizes[size])
print(total)