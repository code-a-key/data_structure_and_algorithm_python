"""
LCM of TWO NUMBER

Find the least common multiple of a given numbers

IP: M = 15 N = 25
OP: 75

TC: O(log(min(m,n)))
SC: O(log(min(m,n)))
"""

def gcd(num1: int, num2: int)-> int:
    """GCD of two number

    Args:
        num1 (int): 1st number
        num1 (int): 2nd number

    Returns:
        int: GCD(num1, num2)
    """
    if num1:
        return num2
    return gcd(num2 % num1, num1)

def lcm(num1: int, num2: int)-> int:
    """LCM of two number

    Args:
        num1 (int): 1st number
        num1 (int): 2nd number

    Returns:
        int: LCM(num1, num2)
    """
    return int((num1 * num2) / gcd(num1, num2))

if __name__ == '__main__':
    M = int(input("Enter the first number: "))
    N = int(input("Enter the second number: "))

    print(f'LCM of {M} and {N} is {lcm(M, N)}')
