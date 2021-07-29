'''
backtracking의 중요 관점
'가지치기'
재귀적 호출로 구현하면서 조건을 만족하면 return하며 원하는 답을 도출한 후
stack의 마지막을 pop하며 다음 loop를 재귀적으로 진행

29200 KB	228 ms
'''

import sys


def bt(arr: list, n: int, m: int):
    if(len(arr) == m):
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        if i in arr:
            continue
        arr.append(i)
        bt(arr, n, m)
        arr.pop()


input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
bt(arr, n, m)
