# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:12:26 2022

@author: Akshatha
"""
def reverse(num):
    list_of_digits =[]
    temp = abs(num)
    rev_num = 0
    while temp !=0:
        list_of_digits.append(temp%10)
        temp = temp //10
    digit_len = len(list_of_digits)-1
    for i,digit in enumerate(list_of_digits):
        rev_num += digit * pow(10,digit_len-i)
    if num < 0:
        rev_num = -rev_num      
    return rev_num

if __name__ == '__main__':
    num1 = 120
    num2 = 123
    num3 = -123
    print(reverse(num3))