"""
GCD of TWO NUMBERS | OTHER METHODS

Calculate the greatest common divisior of two number

IP: M = 8, N = 6
OP: 2
Explaination:
8 = 4*2*1
6 = 3*2*1
GCD(8, 6) = 2

TC: O(log(min(m,n)))
SC: O(log(min(m,n)))
"""

def gcd(num1: int,num2: int)-> int:
    """GCD of two number

    Args:
        num1 (int): 1st number
        num1 (int): 2nd number

    Returns:
        int: GCD(num1, num2)
    """
    if num1 < num2:
        (num1, num2) = (num2, num1)

    if num1 % num2:
        return num2

    return gcd(num2, num1 % num2)


if __name__ == '__main__':
    M = int(input("Enter the first number: "))
    N = int(input("Enter the second number: "))

    print(f"gcd({M}, {N}) = {gcd(M, N)}")

# OTHER METHODS

# Euclid Algorithm...
# def gcd(num1: int, num2: int)-> int:
#     if num1 < num2:   # Assume num1 >= num2
#         (num1, num2) = (num2, num1)

#     if num1 % num2:
#         return num2
#     else:
#         diff = num1 - num2
#         return gcd(max(num2, diff), min(num2, diff))

# def gcd(num1: int,num2: int)-> int:
#     if num1 < num2:
#         (num1, num2) = (num2, num1)

#     while num1 % num2:
#         diff = num1 - num2
#         (num1, num2) = (max(num2, diff), min(num2, diff))

#     return num2
