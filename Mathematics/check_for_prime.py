from math import sqrt

def check_prime(n):
    # add code here
    if n == 1:
        return False
    factor = 0
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            factor += 1
    if factor == 0:
        return True
    return False


n = int(input("Enter a number to check prime..."))
if check_prime(n):
    print(f'the number {n} is Prime.')
else:
    print(f'The number {n} is not Prime.')


