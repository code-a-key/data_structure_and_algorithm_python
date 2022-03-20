def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    s = 2
    while s*s <= n:
        if prime[s]:
            for i in range(s*s, n + 1, s):
                prime[i] = False
        s += 1
    for i in range(2,n+1):
        if prime[i]:
            print(i, end='\t')

print(f"All the prime numbers upto 100 is")
sieve_of_eratosthenes(100)