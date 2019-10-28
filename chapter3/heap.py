#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: Implement heap sort
class HeapTree(object):
    def __init__(self):
        self.a = []

    def push(self, value):
        self.a.append(value)
        # TODO: Extract function
        x = len(self.a) - 1
        while x > 0:
            y = self._parent(x)
            if self.a[y] >= self.a[x]:
                break
            self.a[y], self.a[x] = self.a[x], self.a[y]
            x = y

    def pop(self):
        n = len(self.a) - 1
        if n == 0:
            return self.a.pop()
        self.a[0], self.a[n] = self.a[n], self.a[0]
        # TODO: Extract function
        x = 0
        left = self._left(x)
        right = self._right(x)
        while left < n:
            if right < n and (self.a[right] > self.a[x] or\
                              self.a[left] > self.a[x]):
                if self.a[right] > self.a[left]:
                    self.a[x], self.a[right] = self.a[right], self.a[x]
                    x = right
                else:
                    self.a[x], self.a[left] = self.a[left], self.a[x]
                    x = left
            elif self.a[left] > self.a[x]:
                self.a[x], self.a[left] = self.a[left], self.a[x]
                x =  left
            else:
                break
            left = self._left(x)
            right = self._right(x)
        return self.a.pop()

    def _parent(self, x):
        return (x + 1) // 2 - 1

    def _left(self, x):
        return 2 * x + 1

    def _right(self, x):
        return 2 * (x + 1)

def main():
    h = HeapTree()
    a = [8, 5, 7, 3, 10, 9, 6, 1, 20]
    for i in a:
        print(f'push {i}')
        h.push(i)
        print(h.a)
    for i in a:
        print(f'h.pop() = {h.pop()}')
        print(h.a)

if __name__ == '__main__':
    main()
