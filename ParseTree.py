# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#
import operator
from pythonds.basic import Stack
from BinaryTree import BinaryTree


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
