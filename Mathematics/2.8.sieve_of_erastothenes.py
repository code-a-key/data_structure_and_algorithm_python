"""
SIEVE OF ERATOSTHENES

Used to find prime numbers upto the asked number.

IP: limit = 100
OP: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

TC: O(n*log(log(n)))
SC: O(n)
"""
from typing import List

def sieve_of_eratosthenes(lim: int)-> List[int]:
    """sieve of erastosthenes

    Args:
        lim (int): find prime numbers till lim (limit)

    Returns:
        List[int]: all the prime numbers b/w 2 and lim
    """
    ans = []
    prime = [True for i in range(lim+1)]
    start = 2
    while start * start <= lim:
        if prime[start]:
            for i in range(start * start, lim + 1, start):
                prime[i] = False
        start += 1
    for i in range(2, lim + 1):
        if prime[i]:
            ans.append(i)

    return ans

if __name__ == '__main__':
    limit = int(input("All prime numbers upto: "))
    print("are", sieve_of_eratosthenes(limit))
