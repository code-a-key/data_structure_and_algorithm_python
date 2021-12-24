def count_digit(n):
    """ Iterative Method """
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count 
    """ Recursive Method """
    # if n == 0:
    #     return 0
    # return 1 + count_digit(n//10)
    """ Conversion """
    # n = len(str(n))
    # return n

n = 23965465
print("The number of digits in ", n, "is", count_digit(n))