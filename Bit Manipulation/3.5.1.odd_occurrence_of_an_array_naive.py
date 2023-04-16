"""
Odd Occurrence of a number in an array - Method 1: Naive Method

Given an array arr[] of n integers, find a number which occurred odd times in the array.

IP: arr = [7, 7, 3, 9, 2, 5, 5, 9, 3, 5]
OP: 5

TC: O(n*n)
SC: O(1)
"""
from typing import List

def get_odd_occurrence(arr: List[int]) -> int:
    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        if count % 2 != 0:
            return i
    
    return -1

if __name__ == '__main__':
    arr = [7, 7, 3, 9, 2, 5, 5, 9, 3, 2, 5]
    print(get_odd_occurrence(arr=arr))