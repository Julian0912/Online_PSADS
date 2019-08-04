# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#
from pythonds.basic import Deque


def palindrome_checker(string):
    """判断一个字符串是不是回文字符串

    :param string: str
    :return: bool
    """
    d = Deque()
    for s in string:
        d.addRear(s)
    while d.size() > 1:
        first = d.removeFront()
        last = d.removeRear()
        if first != last:
            return False
    return True


if __name__ == '__main__':
    c = 'radar'
    print(palindrome_checker(c))
