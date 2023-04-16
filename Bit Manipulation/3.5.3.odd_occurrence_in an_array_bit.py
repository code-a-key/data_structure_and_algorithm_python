"""
Odd Occurrence of a number in an array - Method 3: Using Bit Manipulation

Given an array arr[] of n integers, find a number which occurred odd times in the array.

IP: arr = [7, 7, 3, 9, 2, 5, 5, 9, 3, 5]
OP: 5

TC: O(n)
SC: O(1)
"""
from typing import List

def get_odd_occurrence(arr: List[int]) -> int:
    res = 0
    for i in arr:
        res = res ^ i
    return res

if __name__ == '__main__':
    arr = [7, 7, 3, 9, 2, 5, 5, 9, 3, 2, 5]
    print(get_odd_occurrence(arr=arr))