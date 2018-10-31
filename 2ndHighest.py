# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:46:02 2018

@author: Administrator
"""
lst=[-57,-57,57,57,57,57]
#lst=[2,5]
first=second=-2147483648
print("Length of list",lst.__len__())
if(lst.__len__()<=1):
    print("List with only one number")
elif(lst.__len__()==2):
    first=second=lst[0]
    for item in lst:
        if(item>first):
            first=item
        else:
            second=item
else:
    for item in lst:
        if(item>first):
            second=first
            first=item
        elif(item>second and item!=first and first!=second):
            second=item
print(lst,"\nLargest Number:\n",first,"\nSecond Largest:\n",second)