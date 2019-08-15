# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#


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

    # def get_root(self):
    #     return self.root
    #
    # def get_left_child(self):
    #     return self.left_child
    #
    # def get_right_child(self):
    #     return self.right_child

    def insert_left(self, e):
        """插入左孩子，如果已存在左孩子，则将左孩子作为新结点的左孩子"""
        if self.is_empty():
            raise ValueError('the binary tree does not have a root')
        if isinstance(e, BinaryTree):
            subtree = e
        else:
            subtree = BinaryTree(e)
        if self.left_child is not None:
            subtree.left_child = self.left_child       # 此处的插入法有缺陷，要插只能插一个根结点，下同
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


def pre_order(tree: BinaryTree):
    if tree:
        print(tree.root)
        pre_order(tree.left_child)
        pre_order(tree.right_child)


def in_order(tree: BinaryTree):
    if tree:
        in_order(tree.left_child)
        print(tree.root)
        in_order(tree.right_child)


def post_order(tree: BinaryTree):
    if tree:
        post_order(tree.left_child)
        post_order(tree.right_child)
        print(tree.root)
