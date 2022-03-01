# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:59:07 2022

@author: Akshatha
"""

class Solution(object):
    def check_repetition(self, sub_str):
        if len(sub_str) == 1:
            return False
        for letter in sub_str[:-1]:
            if sub_str[-1] == letter:
                return True
        return False           
    
    def lengthOfLongestSubstring(self, arr):
        start = 0
        end = 1
        length = 0
        while start <= len(arr)-1 and end <= len(arr):
            sub_str = arr[start:end]
            while self.check_repetition(sub_str):
                start += 1
                sub_str = arr[start:end]
            if len(sub_str) > length:
                length = len(sub_str)
            end += 1
        return length

if __name__ =='__main__':
    S = Solution()
    str1 = "pwwkew"
    str2 = "abcabcbb"
    str3 = "bbbbb"
    length = S.lengthOfLongestSubstring(str2)
    print(length)