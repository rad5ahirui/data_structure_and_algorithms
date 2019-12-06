#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Just use list in Python.
class Stack(object):
    def __init__(self, n):
        self.a = [None] * n
        self.n = n
        self.top = 0

    def push(self, x):
        assert self.top != self.n
        self.a[self.top] = x
        self.top += 1

    def pop(self):
        assert self.top != 0
        self.top -= 1
        return self.a[self.top]

    def empty(self):
        return self.top == 0

def main():
    n = 5
    stack = Stack(n)
    for i in range(n):
        print(f'push {i}')
        stack.push(i)
    for i in range(n):
        print(f'pop {stack.pop()}')

if __name__ == '__main__':
    main()
