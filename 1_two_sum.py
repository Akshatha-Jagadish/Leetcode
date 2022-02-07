# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 00:13:43 2022

@author: Akshatha
"""
def find(arr, ele):
    for idx, value in enumerate(arr):
        if ele == value:
            return idx
    return -1

def two_sum(nums, target):
    first_idx = 0
    while first_idx < len(nums):
        other = find(nums, target-nums[first_idx])
        if other != first_idx:
            return sorted([first_idx, other])
        first_idx += 1
        
if __name__ == '__main__':
    nums = [3,3]
    target = 6
    print(two_sum(nums,target))