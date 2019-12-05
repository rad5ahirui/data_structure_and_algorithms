#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from p6_2 import Stack
from p6_3 import Queue

class A(ABC):
    @abstractmethod
    def add(self, x):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def empty(self):
        pass

class AStack(A):
    def __init__(self, n):
        self.stack = Stack(n)

    def add(self, x):
        self.stack.push(x)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return self.stack.empty()

class AQueue(A):
    def __init__(self, n):
        self.que = Queue(n)

    def add(self, x):
        self.que.insert(x)

    def pop(self):
        return self.que.get()

    def empty(self):
        return self.que.empty()

def graph_search(initial_v, T, a):
    # a must be empty
    b = set() # visited
    a.add(initial_v)
    b.add(initial_v)
    while not a.empty():
        v = a.pop()
        print(f'{v} -> ', end='')
        for u in T[v]:
            if u not in b:
                a.add(u)
                b.add(u)
    print('END')
    return b

def main():
    T = [[1, 2], [3, 4], [5], [], [], [6], []]
    print('(1)')
    print(graph_search(0, T, AQueue(len(T))))
    print('(2)')
    print(graph_search(0, T, AStack(len(T))))

if __name__ == '__main__':
    main()
