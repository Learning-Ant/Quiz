'''
기본적 로직은 15649 번 문제와 동일
중복이 가능하므로 loop를 돌 때 stack에 이미 들어있는지 확인할 필요가 없음
if문을 빼주면 정답이다.

29200 KB	1812 ms
'''


import sys


def bt(arr: list, n: int, m: int):
    if(len(arr) == m):
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        arr.append(i)
        bt(arr, n, m)
        arr.pop()


input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
bt(arr, n, m)
