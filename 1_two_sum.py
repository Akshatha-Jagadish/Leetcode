# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 00:13:43 2022

@author: Akshatha
"""
class Solution(object):
    def find(self, arr, ele):
        for idx, value in enumerate(arr):
            if ele == value:
                return idx
        return -1

    def twoSum(self, nums, target):
        first_idx = 0
        while first_idx < len(nums):
            other = self.find(nums, target-nums[first_idx])
            if other != first_idx and other != -1:
                return sorted([first_idx, other])
            first_idx += 1
        
if __name__ == '__main__':
    S = Solution()
    nums = [3,2,3]
    target = 6
    print(S.twoSum(nums,target))