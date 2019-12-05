#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Queue(object):
    def __init__(self, n):
        self.a = [None] * n
        self.head = 0
        self.tail = 0

    def insert(self, x):
        self.a[self.tail] = x
        self.tail += 1
        self.tail %= len(self.a)

    def get(self):
        ret = self.a[self.head]
        self.head += 1
        self.head %= len(self.a)
        return ret

    def empty(self):
        return self.head == self.tail

def main():
    n = 5
    que = Queue(n)
    for i in range(n):
        print(f'insert {i}')
        que.insert(i)
    for i in range(n):
        print(f'get {que.get()}')

if __name__ == '__main__':
    main()
