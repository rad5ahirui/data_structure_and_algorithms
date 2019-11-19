#!/usr/bin/env python3
# coding: utf-8

a = []
b = []
c = []

def move(n, x, y, z):
    if n > 0:
        move(n - 1, x, z, y)
        z.append(x.pop())
        print('Move:', a, b, c,sep='\n')
        move(n - 1, y, x, z)

def main():
    global a
    a = [3, 2, 1]
    print(a, b, c,sep='\n')
    move(3, a, b, c)

if __name__ == '__main__':
    main()
