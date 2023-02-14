"""
COUNT DIGITS METHOD - I: Iterative Method

Given a number count the number of digits

IP: 65415
OP: 5

IP: 787878
OP: 6

TC: O(log10(n))
SC: O(1)
"""

def count_digit(num: int)-> int:
    """ Iterative Method

    Args:
        num (int): number to count digits of

    Returns:
        int: Number of digits in a number
    """
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

if __name__ == '__main__':
    N = int(input('Enter the number: '))
    print("The number of digits in ", N, "is", count_digit(N))
