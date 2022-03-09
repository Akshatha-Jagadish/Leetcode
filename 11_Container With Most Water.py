# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:31:26 2022

@author: Akshatha
"""
class Solution():
    def maxArea(self, num_list):
        area = 0
        l = 0
        r = len(num_list) - 1
        while l < r:
            temp_area = min(num_list[l],num_list[r])*(r-l)
            area = max(temp_area, area)
            if num_list[l] < num_list[r]:
                l += 1
            else:
                r -= 1
        return area

if __name__ == '__main__':
    S = Solution()
    num_list1 = [1,8,6,2,5,4,8,3,7]
    num_list2 = [1,1]
    print(S.maxArea(num_list1))