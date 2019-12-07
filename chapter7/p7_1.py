#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('../chapter3')
from heap import HeapTree

INF = 10 ** 8

def shortest_path(edges, s, t):
    d = [INF] * len(edges)
    prev = [None] * len(edges)
    d[s] = 0
    A = HeapTree()
    A.heapify([(-e, i) for i, e in enumerate(d)])
    while True:
        dv, v = A.pop()
        print(f'v = {v}')
        if v == t:
            path = [v]
            w = prev[v]
            while w != s:
                path.append(w)
                w = prev[w]
            path.append(s)
            return -dv, path
        for w, lvw in edges[v].items():
            print(f'    w = {w}')
            if d[w] == INF:
                d[w] = d[v] + lvw
                print(f'        d[{w}] updated')
                prev[w] = v
                A.push((-d[w], w))
                print(f'        {w} pushed')
            elif d[w] > d[v] + lvw:
                prev[w] = v
                d[w] = d[v] + lvw
                print(f'        d[{w}] updated')

def main():
    n = int(sys.stdin.readline())
    edges = [dict() for i in range(n)]
    for line in sys.stdin.readlines():
        u, v, d = (int(e) for e in line.split())
        edges[u][v] = d
    d, path = shortest_path(edges, 0, 6)
    print()
    print(f'd = {d}')
    print(f'path: {list(reversed(path))}')

if __name__ == '__main__':
    main()
