#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Reference: https://www.slideshare.net/iwiwi/2-12188757

import random

INF = 1e10

class RbstNode(object):
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value
        self._cnt = 1
        self._min = value

    def update(self):
        self._cnt = RbstNode.count(self.left) + \
            RbstNode.count(self.right) + 1
        self._min = min(min(RbstNode.min(self.left),
                            RbstNode.min(self.right)),
                        self.value)
        return self

    @classmethod
    def merge(cls, left, right):
        if left is None or right is None:
            if left is None:
                return right
            return left
        if random.randint(1, INF) % \
           (RbstNode.count(left) + RbstNode.count(right)) < \
           RbstNode.count(left):
            left.right = RbstNode.merge(left.right, right)
            return left.update()
        right.left = RbstNode.merge(left, right.left)
        return right.update()

    @classmethod
    def split(cls, node, key):
        if node is None:
            return None, None
        if key <= RbstNode.count(node.left):
            l, r = RbstNode.split(node.left, key)
            node.left = r
            return l, node.update()
        l, r = RbstNode.split(node.right,
                               key - RbstNode.count(node.left) - 1)
        node.right = l
        return node.update(), r

    @classmethod
    def traverse(cls, n):
        if n is None:
            return
        RbstNode.traverse(n.left)
        print(n.key, n.value, n._min)
        RbstNode.traverse(n.right)

    @classmethod
    def min(cls, node):
        if node is None:
            return INF
        return node._min

    @classmethod
    def count(cls, node):
        if node is None:
            return 0
        return node._cnt

class Rbst(object):
    def __init__(self):
        self._root = None

    def merge(self, tree):
        if tree is None:
            return self
        self._root = RbstNode.merge(self._root, tree._root)
        return self

    def split(self, key):
        right = Rbst()
        left = Rbst()
        left._root, right._root = RbstNode.split(self._root, key)
        return left, right

    def insert(self, key, value):
        node = RbstNode(key, value)
        left, right = RbstNode.split(self._root, key)
        self._root = RbstNode.merge(RbstNode.merge(left, node), right)

    def erase(self, key):
        left, tmp = RbstNode.split(self._root, key - 1)
        mid, right = RbstNode.split(tmp, key - RbstNode.count(left))
        self._root = RbstNode.merge(left, right)

    def find(self, key):
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None

    def min(self, p, q):
        if self._root is None:
            return INF
        n = RbstNode.count(self._root)
        x, y = RbstNode.split(self._root, p)
        z, w = RbstNode.split(y, q - p + 1)
        ret = RbstNode.min(z)
        RbstNode.merge(x, RbstNode.merge(z, w))
        return ret

    def traverse(self):
        RbstNode.traverse(self._root)

def main():
    # https://qiita.com/okateim/items/e2f4a734db4e5f90e410
    a = [10, 2, 5, 7, 11, 15, 1, 9, 3, 15, 13, 4, 7]
    t = Rbst()
    for i, e in enumerate(a):
        t.insert(i, e)
    print(t.min(4, 8))

if __name__ == '__main__':
    main()
