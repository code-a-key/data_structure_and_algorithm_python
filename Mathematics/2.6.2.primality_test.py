"""
CHECK FOR PRIME | METHOD: PRIMALITY TEST

Check whether the given number is Prime or not.

IP: N = 5
OP: The number 5 is Prime.

IP: N = 10
OP: The number 10 is not Prime.

TC: O(sqrt(n))
SC: O(1)
"""

def check_prime(num: int)-> bool:
    """Check if the number is prime

    Args:
        num (int): number to check

    Returns:
        bool: True if number is Prime, False otherwise
    """
    if num <= 3:
        return num > 1
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i **2 <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i+=6
    return True

if __name__ == '__main__':
    n = int(input("Enter a number to check prime..."))
    if check_prime(n):
        print(f'The number {n} is Prime.')
    else:
        print(f'The number {n} is not Prime.')
