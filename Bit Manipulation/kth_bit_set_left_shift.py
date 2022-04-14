# Problem : Check Kth bit is set or not
# Method 1: Using Left Shift operator

n, k = [int (x) for x in input().split()]
temp = 1 << (k - 1)
if n & temp:
    print("SET")
else:
    print("NOT SET")