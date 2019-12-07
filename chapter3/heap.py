#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class HeapTree(object):
    def __init__(self):
        self.a = []

    def push(self, value):
        self.a.append(value)
        self._upHeap(len(self.a))

    def heapify(self, a):
        self.a = a
        for i in range(len(a)):
            self._upHeap(i)

    def pop(self):
        n = len(self.a) - 1
        if n == 0:
            return self.a.pop()
        self.swapAndDownHeap(n)
        return self.a.pop()

    # 英語わからん
    # Swap a[0] and a[end], then reconstruct the tree from 0 to end.
    def swapAndDownHeap(self, end):
        self.a[0], self.a[end] = self.a[end], self.a[0]
        x = 0
        left = self._left(x)
        right = self._right(x)
        while left < end:
            if right < end and (self.a[right] > self.a[x] or\
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

    def _upHeap(self, end):
        x = end - 1
        while x > 0:
            y = self._parent(x)
            if self.a[y] >= self.a[x]:
                break
            self.a[y], self.a[x] = self.a[x], self.a[y]
            x = y

    def _parent(self, x):
        return (x + 1) // 2 - 1

    def _left(self, x):
        return 2 * x + 1

    def _right(self, x):
        return 2 * (x + 1)

    def __len__(self):
        return len(self.a)

def heap_sorted(a):
    heap = HeapTree()
    for e in a:
        heap.push(e)
    for i in range(len(a) - 1, -1, -1):
        heap.swapAndDownHeap(i)
    return heap.a

def heap_sort(a):
    heap = HeapTree()
    heap.heapify(a)
    for i in range(len(a) - 1, -1, -1):
        heap.swapAndDownHeap(i)

def main():
    a = [8, 5, 7, 3, 10, 9, 6, 1, 20]
    print(a)
    print(heap_sorted(a))
    print(a)
    heap_sort(a)
    print(a)

if __name__ == '__main__':
    main()
