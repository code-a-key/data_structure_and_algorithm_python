# Problem : Check Kth bit is set or not
# Method 1: Using Right Shift operator

n, k = [int (x) for x in input().split()]
temp = n >> (k - 1)
if temp and 1:
    print("SET")
else:
    print("NOT SET")