'''
일단 단순히 2중 for 문으로 모든 원소들을 비교할 수도 있지만,
좀 더 시간을 줄이기 위해 두 리스트를 정렬해 이진탐색으로 수행할 수도 있다.
이진탐색으로 A 리스트의 특정요소보다 작은 B 리스트의 요소의 '인덱스'를 찾는다.
그렇게 찾은 인덱스를 활용하면 해당 요소보다 작은 수의 개수를 쉽게 찾을 수 있다.

여기서, 두 리스트가 이미 정렬되어 있으므로 A 리스트의 특정요소보다 작은 B 리스트의 요소 개수를 찾았으니,
A 리스트의 다음 요소일 경우에 B 리스트를 탐색할 경우 그 이전 요소가 탐색을 마친 이후의 위치부터 탐색할 수 있다.
이를 dp를 통해 구현할 수 있을 것이다.

즉, binary search + dynamic programming인 문제
'''

import sys
input = sys.stdin.readline

biSearch(numbsers:list, target:int):


tc = int(input())

for _ in range(tc) :
  n, m = map(int, input().strip().split())
  nl = sorted(list(map(int, input().strip().split())))
  ml = sorted(list(map(int, input().strip().split())))
  cnt = 0
  for i in range(n):
    
    
  print(cnt)
