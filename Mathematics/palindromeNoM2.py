num = int(input("Enter the num:"))
num_str = str(num)
rev = num_str[::-1]
if rev == num_str:
    print('YES')
else:
    print('NO')
