# -*- coding:utf8 -*-
# Author: Julian Black
# Description: 多种排序方法；无特殊说明，参数均为无序数组，排序后均为递增数组
#


def bubble_sort(ul):
    """冒泡排序

    :param ul: List[int]
    :return: List[int]
    """
    for p in range(len(ul) - 1, 0, -1):  # 一共循环n-1次
        for i in range(p):
            if ul[i] > ul[i + 1]:
                ul[i], ul[i + 1] = ul[i + 1], ul[i]


def short_bubble_sort(ul):
    """短冒泡排序，对于有序度高的数组更省时间

    :param ul: List[int]
    :return: List[int]
    """
    exchanges = True
    p = len(ul) - 1
    while p > 0 and exchanges:
        exchanges = False
        for i in range(p):
            # 如果对于某一次pass，后面的所有数字都没发生过交换（没有执行if语句）
            # 说明后面所有数字都是有序的，则不需要再遍历了（exchanges为False，跳出while）
            if ul[i] > ul[i + 1]:
                exchanges = True  # 如果有交换，就需要再遍历至少一次
                ul[i], ul[i + 1] = ul[i + 1], ul[i]
        p -= 1


def selection_sort(ul):
    """选择排序

    :param ul: List[int]
    :return: List[int]
    """
    for tar_pos in range(len(ul) - 1, 0, -1):  # tar_pos是此次pass中最大值应该在的位置
        pos_of_max = 0  # 假设此次pass最大值的位置为索引0
        for i in range(1, tar_pos + 1):  # 对于剩下的所有索引，都要遍历一遍与‘最大值’比较
            if ul[i] > ul[pos_of_max]:  # 如果大，就更新最大值索引
                pos_of_max = i
        # 最后把最大值位置和目标位置换一下
        ul[pos_of_max], ul[tar_pos] = ul[tar_pos], ul[pos_of_max]


if __name__ == '__main__':
    unordered_ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # check_ls = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
    nearly_sorted_ls = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]  # 有序度高
    check_ls2 = [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
    # bubble_sort(unordered_ls)
    # short_bubble_sort(nearly_sorted_ls)
    selection_sort(check_ls2)
    print(check_ls2)
