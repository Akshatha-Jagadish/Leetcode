# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:23:20 2022

@author: Akshatha
"""
class Solution(object):
    def reverse(self,num):
        list_of_digits =[]
        temp = abs(num)
        rev_num = 0
        while temp !=0:
            list_of_digits.append(temp%10)
            temp = temp //10
        digit_len = len(list_of_digits)-1
        for i,digit in enumerate(list_of_digits):
            rev_num += digit * pow(10,digit_len-i)   
        # print(rev_num)
        return rev_num
    
    def isPalindrome(self,num):
        if num < 0:
            return False
        if num == self.reverse(num):
            return True
        return False

if __name__ == '__main__':
    S = Solution()
    num1 = 121
    num2 = -121
    num3 = 10
    # print(num2)
    print(num2, S.isPalindrome(num2))