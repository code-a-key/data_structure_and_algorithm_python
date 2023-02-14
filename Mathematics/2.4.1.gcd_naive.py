"""
GCD of TWO NUMBERS | METHOD - I: NAIVE

Calculate the greatest common divisior of two number

IP: M = 8, N = 6
OP: 2
Explaination:
8 = 4*2*1
6 = 3*2*1
GCD(8, 6) = 2

TC: O(min(m,n))
SC: O(1)
"""

def gcd(num1: int, num2: int)-> int:
    """GCD of two number - Naive

    Args:
        num1 (int): 1st number
        num1 (int): 2nd number

    Returns:
        int: GCD(num1, num2)
    """

    factor_num1 = []
    for i in range(1, num1+1):
        if num1%i:
            factor_num1.append(i)

    factor_num2 = []
    for j in range(1, num2+1):
        if num2 % j:
            factor_num2.append(j)

    common_factors = []
    for i in factor_num1:
        if i in factor_num2:
            common_factors.append(i)
    return common_factors[-1]

if __name__ == '__main__':
    M = int(input("Enter the first number: "))
    N = int(input("Enter the second number: "))

    print(f"gcd({M}, {N}) = {gcd(M, N)}")
