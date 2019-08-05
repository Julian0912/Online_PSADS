# -*- coding:utf8 -*-
# Author: Julian Black
# Description: 多种排序方法；无特殊说明，参数均为无序数组，排序后均为递增数组
#


def bubble_sort(ul):
    """冒泡排序

    :param ul: List[int]
    """
    for p in range(len(ul) - 1, 0, -1):  # 一共循环n-1次
        for i in range(p):
            if ul[i] > ul[i + 1]:
                ul[i], ul[i + 1] = ul[i + 1], ul[i]


def short_bubble_sort(ul):
    """短冒泡排序，对于有序度高的数组更省时间

    :param ul: List[int]
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
    """
    for tar_pos in range(len(ul) - 1, 0, -1):  # tar_pos是此次pass中最大值应该在的位置
        pos_of_max = 0  # 假设此次pass最大值的位置为索引0
        for i in range(1, tar_pos + 1):  # 对于剩下的所有索引，都要遍历一遍与‘最大值’比较
            if ul[i] > ul[pos_of_max]:  # 如果大，就更新最大值索引
                pos_of_max = i
        # 最后把最大值位置和目标位置换一下
        ul[pos_of_max], ul[tar_pos] = ul[tar_pos], ul[pos_of_max]


def insertion_sort(ul, start=0, gap=1):
    """插入排序

    gap: 子数组的索引间隔，例数组array[5]，gap=2，则两个子数组的索引为0,2,4和1,3
    start: 子数组的第一个索引，如上例为0和1

    **仅作插入排序时不需要修改默认值，在希尔排序内使用时需要修改默认值**
    **注释在解释时使用了默认值**

    :param ul: List[int]
    :param start: int
    :param gap: int
    """
    for index in range(start + gap, len(ul), gap):  # 假设数组第一个值为一个有序数组，则从第二个值开始
        cur = ul[index]  # 存储当前值
        pos = index  # 向前跑动的游标
        while pos >= gap and ul[pos - gap] > cur:  # 在游标到头之前，如果游标前一个值比当前值大
            ul[pos] = ul[pos - gap]  # 就把前一个值后移一位（覆盖了当前值，留出了一个空位）
            pos -= gap  # 游标前移一位
        ul[pos] = cur  # 空位会一直向后移动，直到游标前一个值比当前值小，则把当前值插入空位
        # 注：空位实际还是有值


def shell_sort(ul):
    """希尔排序

    先将数组分割成几个子数组，每个分别作插入排序，
    然后减小gap，当gap减小到1时，即是一次完整的插入排序，
    但因为之前的操作已经使数组有序度提高，所以在实际时间上会节省一些

    :param ul: List[int]
    """
    sublist_count = len(ul) // 2  # 这只是希尔排序分割数组的其中一种方式
    while sublist_count > 0:
        for start_pos in range(sublist_count):
            insertion_sort(ul, start_pos, sublist_count)
        sublist_count //= 2  # 重点是让gap减小到1


def merge_sort(ul):
    """归并排序

    :param ul: List[int]
    """
    if len(ul) > 1:  # 对于长度小于等于1的数组不需要排序，也是递归地截至条件
        mid = len(ul) // 2
        left = ul[:mid]
        right = ul[mid:]
        merge_sort(left)  # 此处递归调用后可以认为left子数组已经有序
        merge_sort(right)  # 同上
        l, r, k = 0, 0, 0
        while l < len(left) and r < len(right):
            # 此处选出left和right中小的那个依次覆盖原数组，加等号有利于稳定性
            if left[l] <= right[r]:
                ul[k] = left[l]
                l += 1
            else:
                ul[k] = right[r]
                r += 1
            k += 1
        # 然后两个数组中必定有一个数组剩余至少一个值（最大的那些）
        # 循环只会执行一个
        while l < len(left):
            ul[k] = left[l]
            l += 1
            k += 1
        while r < len(right):
            ul[k] = right[r]
            r += 1
            k += 1


def quick_sort(ul):
    """快速排序

    返回新数组

    :param ul: List[int]
    :return List[int]
    """
    if len(ul) <= 1:
        return ul
    mid = len(ul) // 2
    temp = sorted([ul[0], ul[mid], ul[-1]])  # 用于寻找最佳基数
    pivot = temp[1]
    left, right = [], []
    for i in ul:  # 排除pivot本身
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    unordered_ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # check_ls = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
    nearly_sorted_ls = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]  # 有序度高
    check_ls2 = [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
    # bubble_sort(unordered_ls)
    # short_bubble_sort(nearly_sorted_ls)
    # selection_sort(check_ls2)
    # insertion_sort(unordered_ls)
    # shell_sort(unordered_ls)
    # merge_sort(unordered_ls)
    sorted_ls = quick_sort(unordered_ls)
    # print(unordered_ls)
    print(sorted_ls)
