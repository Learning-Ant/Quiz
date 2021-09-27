'''
브루트 포스와 백트래킹을 이해했다고 생각했는데,
아직 부족한 듯 하다.
혼자 백트래킹으로 풀고자 했었지만 실패, 다른 답변들을 참고해
풀이에 대한 이해는 했지만, 스스로 풀 수 있을지는 아직 확실치 않다.

29200 KB	500 ms
'''

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
n, s = map(int, input().strip().split())

k = list(map(int, input().strip().split()))
cnt = 0

def bt(i, si, n, k, s):
    global cnt
    print(i, si)
    
    if i == n:
        return
    if si + k[i] == s:
        cnt += 1
    
    bt(i + 1, si, n, k, s)
    bt(i + 1, si + k[i], n, k, s)

bt(0, 0, n, k, s)
print(cnt)

''''''''''''''''''''''''''''''''''''''''''''''''
# def bt(a:set, b, c):
#     global cnt
#     if len(a) > 0 and sum(a) == b:
#         print(len(a), sum(a), b)
#         cnt += 1
#         return
#     for i in c:
#         a.add(i)
#         bt(a, b, c)
#         a.remove(i)

# a=set()
# bt(a, s ,k)

# print(cnt)