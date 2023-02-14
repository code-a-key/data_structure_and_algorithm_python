"""
PALINDROME NUMBER | METHOD - II: CONVERT TO STRING AND REVERSE CHECK

Check whether the given number is palindrome or not

IP:565655
OP: NO

IP: 89998
OP: YES

TC: O(log n)
SC: O(1)
"""

def check_palindrome(num: int)-> bool:
    """check_palindrome: Naive

    Args:
        num (int): Number to check

    Returns:
        bool: True if the number is palindrome, False otherwise
    """
    num_str = str(num)
    rev = num_str[::-1]
    return bool(rev == num_str)

if __name__ == '__main__':
    N = int(input("Enter the number: "))
    if check_palindrome(N):
        print("YES")
    else:
        print("NO")
