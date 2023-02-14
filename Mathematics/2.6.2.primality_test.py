def check_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i **2 <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i+=6
    return True


n = int(input("Enter a number to check prime..."))
if check_prime(n):
    print(f'the number {n} is Prime.')
else:
    print(f'The number {n} is not Prime.')
