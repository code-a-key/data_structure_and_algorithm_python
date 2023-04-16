"""
FACTORIAL OF A NUMBER | METHOD - I: RECURSIVE

Find the factorial of the given number.

Base Condition:
1! = 1
0! = 1

IP: N = 6
OP:720
Explaination: ans = 6*5*4*3*2*1 = 720

TC: O(n)
SC: O(n)
"""

def fact(num: int) -> int:
    """factorial of a number

    Args:
        num (int): to find factorial of

    Returns:
        int: factorial of a number
    """
    # Base Condition
    if num in (1, 0):
        return 1

    return num*fact(num-1)

if __name__ == '__main__':
    N = int(input("Enter the number:"))
    print(f"{N}! = {fact(N)}")
