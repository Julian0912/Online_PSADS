# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#
from pythonds.basic import Queue


def hot_potato(names, count):
    """一圈孩子围在一起，一个孩子手里拿着一个热狗，
    从他开始将热狗向旁边人传递，一定次数后踢掉拿着热狗的孩子

    :param names: List[str]
    :param count: int
    :return: str
    """
    q = Queue()
    for n in names:  # 将孩子全部加入队列，队首的孩子拿着热狗
        q.enqueue(n)
    while q.size() > 1:
        for _ in range(count):
            child = q.dequeue()  # 弹出第一个孩子
            q.enqueue(child)  # 加入队尾，相当于传递一次热狗
        q.dequeue()  # 将第一个孩子踢出
    last_child = q.dequeue()  # 最后一个孩子
    return last_child


if __name__ == '__main__':
    children = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    num = 7
    print(hot_potato(children, num))
