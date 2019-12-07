#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('../chapter3')
from heap import HeapTree

INF = 10 ** 8

def shortest_path(edges, s):
    d = [INF] * len(edges)
    prev = [None] * len(edges)
    d[s] = 0
    A = HeapTree()
    A.heapify([(-e, i) for i, e in enumerate(d)])
    while len(A) > 0:
        dv, v = A.pop()
        print(f'v = {v}')
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
    return d

def main():
    n = int(sys.stdin.readline())
    edges = [dict() for i in range(n)]
    for line in sys.stdin.readlines():
        u, v, d = (int(e) for e in line.split())
        edges[u][v] = d
    ds = shortest_path(edges, 0)
    print(f'ds = {ds}')

if __name__ == '__main__':
    main()
