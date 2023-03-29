"""
Check weather the given number is power of 2 or not - Method 3: Brain Kernighan's Algorithm

Check weather the given number is power of 2 or not.

IP: n = 32 [1001]
OP: YES

TC: O(1)
SC: O(1)
"""
# Method 3 - Using Brian Kernighan’s Algorithm
def pow_of_2(num: int)-> bool:
    return num & (num-1) == 0


if __name__ == '__main__':
    N = int(input("Enter the number to check: "))
    if pow_of_2(N):
        print("YES")
    else:
        print("NO")
