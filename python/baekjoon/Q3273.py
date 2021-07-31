'''
문제 제목처럼 배열을 가리키는 포인터 두 개를 가지고
원하는 숫자를 만드는 짝이 몇 개 있는지 판단하는 문제.

문제의 조건이 1초안에 모든 연산을 끝내야하고, 시간 복잡도를 고려하면
n이 100,000일 경우 2중 for문으로 구성할 경우 O(n^2)가 되어 조건을 맞출 수 없다.
=> n^2 : 약 100억의 연산이 필요, 1초는 보통 2억회의 연산이므로 불가능

따라서 배열을 먼저 정렬한 후 포인터를 이동시키며 구해야 조건에 맞출 수 있다.

40724 KB	148 ms
'''

import sys

input = sys.stdin.readline

n = int(input())

arr = sorted(list(map(int, input().split())))
ans = int(input())
lp, rp = 0, n - 1
res = 0

while lp < rp:
    if arr[lp] + arr[rp] == ans:
        res += 1
    if arr[lp] + arr[rp] > ans:
        rp -= 1
        continue
    lp += 1

print(res)
