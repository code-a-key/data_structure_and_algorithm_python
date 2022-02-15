def GCD(a,b):
    if a == 0:
        return b
    return GCD(b%a, a)

def LCM(a, b):
    return int((a*b)/GCD(a,b))


num1 = int(input("Enter the 1st num: "))
num2 = int(input("Enter the 2nd num: "))
print(f'LCM of {num1} and {num2} is {LCM(num1, num2)}')