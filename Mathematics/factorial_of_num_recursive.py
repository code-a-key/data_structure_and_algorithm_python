def fact(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*fact(num-1)

num = int(input("Enter the number:"))
print(f"{num}! = {fact(num)}")