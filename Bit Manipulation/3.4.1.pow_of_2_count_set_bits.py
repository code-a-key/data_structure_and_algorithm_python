"""
Check weather the given number is power of 2 or not - Method 1: Count Set Bits

Check weather the given number is power of 2 or not.

IP: n = 32 [1001]
OP: YES

TC: O(log N)
SC: O(1)
"""
# Method 1 - Count Set Bits
def pow_of_2(num: int)-> bool:
    count = 0
    while num > 0:
        if num & 1 == 1:
            count += 1
        n = n >> 1
    
    return 1 if count == 0 else 0


if __name__ == '__main__':
    N = int(input("Enter the number to check: "))
    if pow_of_2(N):
        print("YES")
    else:
        print("NO")
