# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#


class EmptyError(Exception):
    """专门为对空链表执行删除操作时设计的异常"""
    pass


class Node(object):
    """结点"""
    __slots__ = 'element', 'next'

    def __init__(self, element, next):
        self.element = element
        self.next = next


class LinkedList(object):
    """单向链表

    为了减少时间复杂度，该链表的添加（add()）和删除（pop()）操作默认都在头部
    """

    def __init__(self):
        self.header = Node(None, None)
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add(self, e):
        """在链表头部添加一个结点"""
        node = Node(e, None)
        node.next = self.header.next
        self.header.next = node
        self.size += 1

    def insert(self, p: int, e):
        """在链表p位置插入一个结点，若不存在位置p则报错"""
        if p < 0 or p > self.size:
            raise IndexError('out of index')
        node = Node(e, None)
        i = p
        walk = self.header
        while i > 0:
            walk = walk.next
            i -= 1
        node.next = walk.next
        walk.next = node
        self.size += 1

    def search(self, e):
        """在链表内搜索元素e，并返回索引，若找不到则返回-1"""
        walk = self.header
        i = -1
        while walk is not None:
            if walk.element == e:
                return i
            walk = walk.next
            i += 1
        return -1

    def remove(self, e):
        """移除链表的元素e，若找不到则报错"""
        prev = self.header
        walk = self.header.next
        while walk is not None:
            if walk.element == e:
                prev.next = walk.next
                walk.next = None
                self.size -= 1
                return
            walk = walk.next
            prev = prev.next
        else:
            raise ValueError('element does not exist')

    def pop(self, p: int = 0):
        """移除链表位置p的元素，若不存在位置p则报错"""
        if p < 0 or p >= self.size:
            raise IndexError('out of index')
        walk = self.header
        i = p
        while i > 0:
            walk = walk.next
            i -= 1
        suc = walk.next
        walk.next = suc.next
        suc.next = None
        self.size -= 1
