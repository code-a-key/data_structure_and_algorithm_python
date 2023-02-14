"""
CHECK FOR PRIME

Check whether the given number is Prime or not.

IP: N = 5
OP: The number 5 is Prime.

IP: N = 10
OP: The number 10 is not Prime.

TC: O(sqrt(n))
SC: O(1)
"""

from math import sqrt

def check_prime(num: int) -> bool:
    """Check if the number is prime

    Args:
        num (int): number to check

    Returns:
        bool: True if number is Prime, False otherwise
    """
    # Base Case
    if num <= 1:
        return False
    # Verifying from 2 to sqrt(num)
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input("Enter a number to check prime..."))
    if check_prime(n):
        print(f'The number {n} is Prime.')
    else:
        print(f'The number {n} is not Prime.')
