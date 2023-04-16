"""
Odd Occurrence of a number in an array - Method 2: Using Hashing

Given an array arr[] of n integers, find a number which occurred odd times in the array.

IP: arr = [7, 7, 3, 9, 2, 5, 5, 9, 3, 2, 5]
OP: 5

TC: O(n)
SC: O(n)
"""
from typing import List

def get_odd_occurrence(arr: List[int]) -> int:
    
    size = len(arr)
    _hash = {}
    
    # for i in arr:
    #     if i in _hash:
    #         _hash[i] += 1
    #     else:
    #         _hash[i] = 1
    for i in range(size):
        _hash[arr[i]] = _hash.get(arr[i], 0)+1

    
    for i in _hash:
        if _hash[i] % 2 != 0:
            return i
    return -1

if __name__ == '__main__':
    arr = [7, 7, 3, 9, 2, 5, 5, 9, 3, 2, 5]
    print(get_odd_occurrence(arr=arr))
