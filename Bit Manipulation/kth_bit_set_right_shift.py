"""
CHECK Kth BIT IS SET OR NOT - METHOD 2: USING RIGHT SHIFT OPERATOR (>>)

Check if kth bit is set or not. Using Right Shift Operator (>>)

IP: N = 27 K = 4
OP: SET!

IP: N = 2 K = 3
OP: NOT SET!

TC: O(1)
SC: O(1)
"""

def is_set(num: int, kth: int) -> bool:
    """is_set

    Args:
        num (int): a number given
        kth (int): position of bit to check if its set

    Returns:
        bool: True if kth bit is set otherwise False
    """
    return bool(num >> kth)


if __name__ == '__main__':
    N, K = [int (X) for X in input().split()]
    if is_set(N, K):
        print('SET!')
    else:
        print('NOT SET!')
