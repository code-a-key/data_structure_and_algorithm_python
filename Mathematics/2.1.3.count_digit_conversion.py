"""
COUNT DIGITS METHOD - III: TYPE CONVERSION

Given a number count the number of digits

IP: 65415
OP: 5

IP: 787878
OP: 6

TC: O(1)
SC: O(digits in N)
"""

def count_digit(num: int)-> int:
    """ Type Conversion Method

    Args:
        num (int): number to count digits of

    Returns:
        int: Number of digits in a number
    """
    return len(str(num))


if __name__ == '__main__':
    N = int(input('Enter the number: '))
    print("The number of digits in ", N, "is", count_digit(N))
