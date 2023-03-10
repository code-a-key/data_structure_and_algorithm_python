"""
PALINDROME NUMBER | METHOD - I: NAIVE

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
    rev = 0
    temp = num
    while temp > 0:
        dig = temp % 10
        rev = rev * 10 + dig
        temp = temp // 10
    return bool(num == rev)

if __name__ == '__main__':
    N = int(input("Enter the number: "))
    if check_palindrome(N):
        print("YES")
    else:
        print("NO")
