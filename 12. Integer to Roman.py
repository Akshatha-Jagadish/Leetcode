# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:48:26 2022

@author: Akshatha
"""
class Solution():
    def intToRoman(self,num):
        temp = num
        list_of_digits = []
        while temp !=0:
            list_of_digits.append(temp%10)
            temp = temp //10
        roman = self.convert(list_of_digits)
        return roman
    
    def convert(self, list_of_digits):
        dict_roman = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        roman = ''
        for i,digit in enumerate(list_of_digits):
            if digit < 4:
                roman = dict_roman[1*pow(10,i)]*digit + roman
            elif digit == 4 or digit == 9:
                roman = dict_roman[(digit+1)*pow(10,i)] + roman
                roman = dict_roman[1*pow(10,i)] + roman
            elif digit < 9:
                roman = dict_roman[1*pow(10,i)]*(digit-5) + roman
                roman = dict_roman[5*pow(10,i)] + roman            
        return roman
    
if __name__ == '__main__':
    S = Solution()
    num1 = 60
    print(S.intToRoman(num1))