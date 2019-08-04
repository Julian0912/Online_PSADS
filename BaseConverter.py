# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#
from pythonds.basic import Stack


def converter(number: int, base: int) -> str:
    """进制转换，支持十进制转换为2~16进制"""
    if not (isinstance(number, int) and isinstance(base, int)):
        raise TypeError('type must be both int')
    if not 2 <= base <= 16:
        raise ValueError('base must be among 2 and 16')
    if number < 0:
        raise ValueError('the number must be larger than 0')
    if number == 0:
        return '0'
    s = Stack()
    num_to_alp = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while number != 0:
        remainder = number % base
        if remainder in num_to_alp.keys():
            s.push(num_to_alp[remainder])
        else:
            s.push(remainder)
        number //= base
    res = ''
    for i in range(s.size()):
        res += str(s.pop())
    return res
