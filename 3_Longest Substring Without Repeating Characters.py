# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:59:07 2022

@author: Akshatha
"""

def check_repetition(sub_str):
    if len(sub_str) == 1:
        return False
    for i,letter in enumerate(sub_str):
        for j,letter1 in enumerate(sub_str[i+1:]):
            if letter1 == letter:
                return True
    return False
            

def length_of_longest_substring(arr):
    start = 0
    end = 1
    length = 0
    final_string = ''
    while start <= len(arr)-1 and end <= len(arr):
        sub_str = arr[start:end]
        while check_repetition(sub_str):
            start += 1
            sub_str = arr[start:end]
        if len(sub_str) > length:
            length = len(sub_str)
            final_string = sub_str
        end += 1
    return length, final_string

if __name__ =='__main__':
    str1 = "pwwkew"
    str2 = "abcabcbb"
    str3 = "bbbbb"
    length,long_substr = length_of_longest_substring(str2)
    print(length, long_substr)