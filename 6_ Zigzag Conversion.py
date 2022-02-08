# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 22:32:55 2022

@author: Akshatha
"""

def convert(arr, num_rows):
    new_arrs = ['' for i in range(num_rows)]
    strs = ['' for i in range(num_rows)]
    rev = False
    idx = 0
    prev_str_idx = -1
    while idx < len(arr):
        if rev:
            # strs = strs[::-1]
            for i in range(num_rows-2):
                new_str_idx = prev_str_idx - 1
                for j in range(len(strs)):
                    if j == new_str_idx and idx < len(arr):
                        strs[j] += arr[idx]
                        prev_str_idx = j
                        new_arrs[j] += arr[idx]
                    else:
                        strs[j] += ' '
                idx += 1
            # strs = strs[::-1]
            rev = False
        else:
            for i in range(len(strs)):
                if idx < len(arr):
                    strs[i] += arr[idx]
                    new_arrs[i] += arr[idx]
                    idx += 1
                    prev_str_idx = i
                else:
                    break
            rev = True
    print(new_arrs)
    new_arr = ''.join(new_arrs)
    return strs, new_arr

if __name__ =='__main__':
    str1 = "PAYPALISHIRING"
    num_rows = 3
    strs, new_arr = convert(str1, num_rows)
    for ele in strs:
        print(ele)
    print(new_arr)