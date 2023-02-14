"""
PRIME FACTORS

Find Prime Factors of the given number

IP: 100
OP: [2, 2, 5, 5]

TC: O(sqrt(n))
SC: O(1)
"""

from math import sqrt
from typing import List

def prime_factors(num: int)-> List[int]:
    """prime_factors

    Args:
        num (int): number to find prime factors of

    Returns:
        List[int]: Prime factors of a number
    """
    ans = []

    # Step 1 - Even
    while num % 2 == 0:
        ans.append(2)
        num /= 2

    # Step - 2 - Checking for Odd Composite
    for i in range(3, int(sqrt(num)) + 1, 2):
        while num % i == 0:
            ans.append(i)
            num /= i

    # Step 3 Prime Numbers greater than 2
    if num > 2:
        ans.append(int(num))

    return ans

if __name__ == '__main__':
    N = int(input("Enter the number: "))
    print(f'Prime Factors of {N} is {prime_factors(N)}')
