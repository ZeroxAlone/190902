# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 00:03:17 2019

@author: lisa_
"""

#1

Count = 1
Total = 0
Weighting = 10

while Count != 9:
    Digit = eval(input("Please input a digit: "))
    Value = Digit * Weighting
    Total = Total + Value
    Weighting = Weighting - 1
    Count = Count + 1

Remainder = Total % 11
CheckDigit = 11 - Remainder
if CheckDigit == 10:
     CheckDigit = "X"

print("Chcek digit is: ", CheckDigit)

#2
poscount = 0
negcount = 0
while True:
    number = eval(input("Please input a number: "))
    if number == 0:
        break
    else:
        if number > 0:
            poscount+=1
        else:
            negcount+=1
print("The amount of positive number is: ", poscount)
print("The amount of negative number is: ", negcount)

#3
RogueValue = -1
Total = 0 
Count = 0
Number = eval(input("Please input a number: "))
while Number != RogueValue:
    Count = Count + 1
    Total = Total + Number
    Number = eval(input("Please input a number: "))
    
if Count > 0:
        Average = Total / Count
        print(Average)

#4
UserList = ["xu","sds"]
PasswordList = ["030109","ytuijk"]
MaxIndex = 2
MyUserID = str(input("Please input an UserID: "))
MyPassword = str(input("Please input the Password: "))
UserIdFound = False
LoginOK = False
Index = 0
while Index != MaxIndex and UserIdFound != True:
    
    if UserList[Index] == MyUserID:
        UserIdFound = True
        break
    Index = Index + 1
    
if UserIdFound == True:
    if PasswordList[Index] == MyPassword:
        LoginOK = True

if LoginOK == True:
    print("Login Successful")
else:
    print("User ID and/or password incorrect")














