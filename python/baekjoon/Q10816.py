'''
10815와 유사한 문제
전 문제는 이진 탐색을 이용해 함수를 따로 만들어 풀이했지만,
이번에는 dictionary 타입을 사용해 DP 방식으로 풀었다.
이런것도 dp라고 할 수 있는지.. 음..

112140 KB	1056 ms
'''

import sys
input = sys.stdin.readline

n = int(input())
nl = sorted(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))

ans = dict()

for i in nl:
  if i in ans:
    ans[i] += 1
  else :
    ans[i] = 1

k = ans.keys()

for i in ml:
  if i in k:
    print(ans[i], end=' ')
  else :
    print(0, end=' ')