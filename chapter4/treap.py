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
        self._cnt = TreapNode.count(self.left) + \
            TreapNode.count(self.right) + 1
        self._min = min(min(TreapNode.min(self.left),
                            TreapNode.min(self.right)),
                        self.value)
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
        if key <= TreapNode.count(node.left):
            l, r = TreapNode.split(node.left, key)
            node.left = r
            return l, node.update()
        l, r = TreapNode.split(node.right,
                               key - TreapNode.count(node.left) - 1)
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
    def count(cls, node):
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
        left, tmp = TreapNode.split(self._root, key - 1)
        mid, right = TreapNode.split(tmp, key - TreapNode.count(left))
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

    def min(self, p, q):
        if self._root is None:
            return INF
        n = TreapNode.count(self._root)
        x, y = TreapNode.split(self._root, p)
        z, w = TreapNode.split(y, q - p + 1)
        ret = TreapNode.min(z)
        TreapNode.merge(x, TreapNode.merge(z, w))
        return ret

    def traverse(self):
        TreapNode.traverse(self._root)

def main():
    # https://qiita.com/okateim/items/e2f4a734db4e5f90e410
    a = [10, 2, 5, 7, 11, 15, 1, 9, 3, 15, 13, 4, 7]
    t = Treap()
    for i, e in enumerate(a):
        t.insert(i, e)
    print(t.min(4, 8))

if __name__ == '__main__':
    main()
