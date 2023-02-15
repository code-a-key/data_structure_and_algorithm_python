"""
COUNT SET BITS - Method 1: Naive Method

Count Number of 1's (set bits) in the binary representation of a given integer.

IP: n = 9 [1001]
OP: 2

TC: O(log n)
SC: O(1)
"""
def count_set_bits(num: int) -> int:
    """count set bits

    Args:
        num (int): input number

    Returns:
        int: number of set bits
    """
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

    # return bin(num).count('1')

if __name__ == '__main__':
    N = 36
    print(count_set_bits(N))
