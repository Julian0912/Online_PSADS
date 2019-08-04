# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#


def integer_to_string(n, base):
    """将十进制整数转换成2~16进制的字符串，用递归的方法"""
    if not (isinstance(n, int) and isinstance(base, int)):
        raise TypeError
    if not (2 <= base <= 16):
        raise ValueError
    if n < 0:
        raise ValueError
    operands = '0123456789ABCDEF'
    if n < base:
        return operands[n]
    return integer_to_string(n // base, base) + operands[n % base]


if __name__ == '__main__':
    print(integer_to_string(10, 2))
