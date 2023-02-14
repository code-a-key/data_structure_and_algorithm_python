num = int(input('Enter the number:'))
rev = 0 
temp = num
while temp > 0:
    dig = temp % 10
    rev = rev*10+dig
    temp = temp // 10
if num == rev:
    print('YES')
else:
    print('NO')