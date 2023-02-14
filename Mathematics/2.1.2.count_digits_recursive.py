"""
COUNT DIGITS METHOD - II: Recursive Method

Given a number count the number of digits

IP: 65415
OP: 5

IP: 787878
OP: 6

TC: O(log n)
SC: O(log n)
"""

def count_digit(num: int)-> int:
    """ Recursive Method

    Args:
        num (int): number to count digits of

    Returns:
        int: Number of digits in a number
    """
    if num == 0:
        return 0
    return 1 + count_digit(num//10)


if __name__ == '__main__':
    N = int(input('Enter the number: '))
    print("The number of digits in ", N, "is", count_digit(N))
