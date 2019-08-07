# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#
import operator
from pythonds.basic import Stack


class BinaryTree(object):
    """二叉树

    利用递归思想，只保存根结点、左子树和右子树
    """

    def __init__(self, element=None):  # 确保可以是空树
        self.root = element  # 此处的root存储的是根结点内的元素
        self.left_child = None  # 左右子树实际上也是BinaryTree类型
        self.right_child = None

    def is_empty(self):
        return self.root is None

    def add_root(self, e):
        if not self.is_empty():
            raise ValueError('the binary tree has already had a root')
        self.root = e

    def insert_left(self, e):
        """插入左孩子，如果已存在左孩子，则将左孩子作为新结点的左孩子"""
        if self.is_empty():
            raise ValueError('the binary tree does not have a root')
        if isinstance(e, BinaryTree):
            subtree = e
        else:
            subtree = BinaryTree(e)
        if self.left_child is not None:
            subtree.left_child = self.left_child
        self.left_child = subtree

    def insert_right(self, e):
        """插入右孩子，如果已存在右孩子，则将右孩子作为新结点的右孩子"""
        if self.is_empty():
            raise ValueError('the binary tree does not have a root')
        if isinstance(e, BinaryTree):
            subtree = e
        else:
            subtree = BinaryTree(e)
        if self.right_child is None:
            subtree.right_child = self.right_child
        self.right_child = subtree


def build_parse_tree(expr: str):
    """构建一棵解析树

    expr: 全括号的算数表达式，运算符与数字之间用括号隔开

    :param expr: str
    :return: BinaryTree
    """
    ope_ls = expr.split()
    node_stack = Stack()
    tree = BinaryTree('')
    for e in ope_ls:
        if e == '(':
            tree.left_child = BinaryTree('')
            node_stack.push(tree)
            tree = tree.left_child
        elif e in "+-*/":
            tree.root = e
            tree.right_child = BinaryTree('')
            node_stack.push(tree)
            tree = tree.right_child
        elif e.isdigit():
            tree.root = int(e)
            tree = node_stack.pop()
        elif e == ")":
            if node_stack.isEmpty():
                return tree
            tree = node_stack.pop()


def evaluate(tree: BinaryTree):
    """计算解析树"""
    opers = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv}
    left = tree.left_child
    right = tree.right_child
    if left and right:
        func = opers[tree.root]
        return func(evaluate(left), evaluate(right))
    return tree.root
