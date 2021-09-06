'''
29200 KB	76 ms
'''

import sys

input = sys.stdin.readline
def bt(arr: list, n: int, m: int):
    if(len(arr) == m):
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        if i in arr or (len(arr) >= 1 and arr[-1] > i):
          continue
        arr.append(i)
        bt(arr, n, m)
        arr.pop()

n, m = map(int, input().strip().split())

arr = []

bt(arr, n, m)