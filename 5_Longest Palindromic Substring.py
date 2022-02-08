# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:33:42 2022

@author: Akshatha
"""
def check_palindrome(sub_str):
    if len(sub_str) == 1:
        return True
    for i in range(len(sub_str)//2):
        if sub_str[i] != sub_str[-1-i]:
            return False
    return True
    
def longest_palindrome(arr):
    start = 0
    length = 0
    final_string = ''
    while start <= len(arr)-1:
        end = start+1
        while end <= len(arr):
            sub_str = arr[start:end]
            if check_palindrome(sub_str):
                if len(sub_str) > length:
                    length = len(sub_str)
                    final_string = sub_str
            end += 1
        start += 1
    return length, final_string

if __name__ =='__main__':
    str1 = "babad"
    str2 = "cbbd"
    str3 = "bbbbb"
    length,long_substr = longest_palindrome(str1)
    print(length, long_substr)