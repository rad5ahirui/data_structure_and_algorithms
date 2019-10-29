#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Reference: https://www.slideshare.net/iwiwi/2-12188757

import random

INF = 1e10

class TreapNode(object):
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value
        self.priority = random.random()
        self._cnt = 1
        self._min = value

    def update(self):
        self._cnt = TreapNode._count(self.left) + \
            TreapNode._count(self.right) + 1
        # TODO
        self._min = min(min(TreapNode.min(self.left),
                            TreapNode.min(self.right)),
                        self._min)
        return self

    @classmethod
    def merge(cls, left, right):
        if left is None or right is None:
            if left is None:
                return right
            return left
        if left.priority > right.priority:
            left.right = TreapNode.merge(left.right, right)
            return left.update()
        right.left = TreapNode.merge(left, right.left)
        return right.update()

    @classmethod
    def split(cls, node, key):
        if node is None:
            return None, None
        if key <= TreapNode._count(node.left):
            l, r = TreapNode.split(node.left, key)
            node.left = r
            return l, node.update()
        l, r = TreapNode.split(node.right,
                               key - TreapNode._count(node.left) - 1)
        node.right = l
        return node.update(), r

    @classmethod
    def traverse(cls, n):
        if n is None:
            return
        TreapNode.traverse(n.left)
        print(n.key, n.value, n._min)
        TreapNode.traverse(n.right)

    @classmethod
    def min(cls, node):
        if node is None:
            return INF
        return node._min

    @classmethod
    def _count(cls, node):
        if node is None:
            return 0
        return node._cnt

class Treap(object):
    def __init__(self):
        self._root = None

    def merge(self, tree):
        if tree is None:
            return self
        self._root = TreapNode.merge(self._root, tree._root)
        return self

    def split(self, key):
        right = Treap()
        left = Treap()
        left._root, right._root = TreapNode.split(self._root, key)
        return left, right

    def insert(self, key, value):
        node = TreapNode(key, value)
        left, right = TreapNode.split(self._root, key)
        self._root = TreapNode.merge(TreapNode.merge(left, node), right)

    def erase(self, key):
        left, tmp = TreeNode.split(self._root, key - 1)
        mid, right = TreeNode.split(tmp, key)
        self._root = TreapNode.merge(left, right)

    def find(self, key):
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None

    def min(self):
        return TreapNode.min(self._root)

    def traverse(self):
        TreapNode.traverse(self._root)

def main():
    pass

if __name__ == '__main__':
    main()
