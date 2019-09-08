# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:04:20 2019

@author: lisa_
"""
Lookup = list(input("Please input the Lookup: "))
Startpos = int(input("Start position: "))
NumToChange = int(input("Number to change: "))
n = 0
times = 0
for i in range(Startpos, Startpos+NumToChange+1):
    print("Old char: ", Lookup[i])
    NewChar = str(input("New char: "))
    if NewChar != Lookup[i]:
        times+=1
    Lookup[i] = NewChar
    if n == NumToChange-1:
        break
    else:
        n+=1
        Startpos+=1
print("The number of elements changed is: ", times)
print("The new Lookup is: ", "".join(Lookup))