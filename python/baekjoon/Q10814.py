'''
51012 KB	240 ms
'''

import sys

input = sys.stdin.readline

n = int(input())

userList = sorted([tuple(input().split())
                  for i in range(n)], key=lambda x: int(x[0]))


for i in userList:
    print(' '.join(i[:2]))
