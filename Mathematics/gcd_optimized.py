# Euclid Algorithm...
# def gcd(m, n):
#     if m < n:   # Assume m >= n
#         (m, n) = (n, m)
    
#     if (m%n) == 0:
#         return n
#     else:
#         diff = m-n
#         return gcd(max(n, diff), min(n, diff))

# def gcd(m,n):
#     if m < n:
#         (m, n)=(n,m)
#     while (m%n)!=0:
#         diff = m-n
#         (m, n) = (max(n, diff), min(n, diff))
    
#     return n

def gcd(m,n):
    if m < n:
        (m, n) = (n, m)
    
    if m%n == 0:
        return n
    else:
        return gcd(n, m%n)


m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
print(f"gcd({m}, {n}) = {gcd(m,n)}")