from math import sqrt

def primeFactors(n):
    # Step 1 - Even 
    while n % 2 == 0:
        print(2)
        n = n / 2
    # Step - 2 - Checking for Odd Composite
    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            print(i)
            n /= i
    # Step 3 Prime Numbers greater than 2
    if n > 2:
        print(int(n))

n = 100
primeFactors(n)