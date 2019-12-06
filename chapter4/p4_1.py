#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rbst

class N(rbst.RbstNode):
    @classmethod
    def p(cls, n, x):
        if n is None:
            return
        N.p(n.right, x + 4)
        print(f'{" " * x}{n.value:2}')
        N.p(n.left, x + 4)

class T(rbst.Rbst):
    def p(self):
        N.p(self._root, 0)

def main():
    # The array is already sorted and the size is small, so you can easily
    # construct a balanced binary search tree by hand
    # (子として真ん中の要素を値とするノードを追加し続ければいい).
    a = [
        3, 5, 7, 10, 15, 16, 18, 19, 20,
        23, 24, 33, 35, 40, 41, 42, 46,
    ]
    t = T()
    for i, e in enumerate(a):
        t.insert(i, e)
    t.p()

if __name__ == '__main__':
    main()
