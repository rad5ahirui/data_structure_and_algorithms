#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def h(x, m):
    return x % m

def main():
    a = [
        32, 76, 105, 200, 282,
        888, 28, 168, 56, 1219
    ]
    M = 20
    hash_table = [[] for i in range(M)]
    for e in a:
        hash_table[h(e, M)].append(e)

    for i, x in enumerate(hash_table):
        print(f'{i:2}: {x}')

if __name__ == '__main__':
    main()
