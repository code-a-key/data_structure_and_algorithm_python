"""
Generate power set using bitwise operators


"""
from typing import List, Set

def get_power_set(ip_set: List[str]) -> Set[str]:
    set_size = len(ip_set)
    power_set_size = pow(2, set_size)
    
    result = []
    value = ''
    for counter in range(0, power_set_size):
        for i in range(0, set_size):
            # If the ith bit in counter is set
            if counter & (1 << i):
                value = value + ip_set[i]
        result.append(value)
        value = ''
    
    return set(result)


if __name__ == '__main__':
    s = ['a', 'b', 'c']
    
    power_set = get_power_set(ip_set=s)
    
    print(power_set)