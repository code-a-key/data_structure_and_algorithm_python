"""
Check weather the given number is power of 2 or not - Method 2: Log2 Method

Check weather the given number is power of 2 or not.

IP: n = 32 [1001]
OP: YES

TC: O(1)
SC: O(1)
"""
import math 
# Method 1 - Using Ceil and Floor
def log2(x: int) -> bool:
    return False if x == 0 else (math.log10(x)/math.log10(2))

def pow_of_2(n: int) -> bool:
    return math.ceil(log2(n)) == math.floor(log2(n))


if __name__ == '__main__':
    N = int(input("Enter the number to check: "))
    if pow_of_2(N):
        print("YES")
    else:
        print("NO")