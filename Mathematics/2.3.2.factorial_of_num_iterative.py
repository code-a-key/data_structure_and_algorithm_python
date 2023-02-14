"""
FACTORIAL OF A NUMBER | METHOD - II: ITERATIVE

Find the factorial of the given number.

Base Condition:
1! = 1
0! = 1

IP: N = 6
OP:720
Explaination: ans = 6*5*4*3*2*1 = 720

TC: O(n)
SC: O(1)
"""

def fact(num: int)-> int:
    """factorial of a number

    Args:
        num (int): to find factorial of

    Returns:
        int: factorial of a number
    """
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return f"{num}! = {factorial}"


if __name__ == '__main__':
    N = int(input("Enter the number:"))
    if N < 0:
        print("Factorial of -ve number does not exists...")
    else:
        print(fact(N))
