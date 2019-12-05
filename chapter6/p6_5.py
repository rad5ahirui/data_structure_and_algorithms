#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from p6_1 import AQueue, AStack, graph_search

def main():
    T = [
        [1, 10],              # 0
        [0, 2, 11],           # 1
        [1, 3, 12],           # 2
        [2, 4, 12, 13],       # 3
        [3, 5],               # 4
        [4, 6, 8, 12],        # 5
        [5, 7],               # 6
        [6, 8],               # 7
        [5, 7, 9, 13],        # 8
        [8, 10, 11, 12, 13],  # 9
        [0, 9, 11],           # 10
        [1, 9, 10, 12],       # 11
        [2, 3, 5, 9, 11, 13], # 12
        [3, 8, 9, 12],        # 13
    ]
    print('Queue')
    print(graph_search(0, T, AQueue(len(T))))
    print('Stack')
    print(graph_search(0, T, AStack(len(T))))

if __name__ == '__main__':
    main()
