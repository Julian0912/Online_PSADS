# -*- coding:utf8 -*-
# Author: Julian Black
# Function: 
#


def binary_search(sorted_list: list, target: int) -> bool:
    """二分查找，非递归，列表递增"""
    first = 0
    last = len(sorted_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if sorted_list[middle] == target:
            return True
        elif sorted_list[middle] < target:
            first = middle + 1
        else:
            last = middle - 1
    else:
        return False


if __name__ == '__main__':
    ls = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    for i in range(43):
        print(i, binary_search(ls, i))

