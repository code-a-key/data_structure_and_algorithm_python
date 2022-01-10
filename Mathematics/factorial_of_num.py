num = int(input("Enter the number:"))
fact = 1
if num < 0:
    print("Factorial of -ve number does not exists...")
else:
    for i in range(1, num+1):
        fact = fact*i
    print(f"{num}! = {fact}")
