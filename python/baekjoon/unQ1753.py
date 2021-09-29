'''
풀이
그동안은 인접 리스트로만 그래프 관련 문제를 풀어왔다.
이번에는 인접 배열을 통해 풀어보고자 한다.

인접 배열의 인덱스는 각각의 정점을 의미하고,
해당 위치에 저장되는 값은 행 인덱스에서 열 인덱스로 가는 경로의 최소 가중치를 가지게 되도록 알고리즘을 구성한다.

'''

import sys

input = sys.stdin.readline

v, e = map(int, input().strip().split())
sNode = int(input().strip())
# edge (from, to, weight)
eList = [tuple(map(int, input().strip().split())) for _ in range(e)]

eMap = [[float('inf')] * v for i in range(v)]

print(eMap)
# for i in range(e):