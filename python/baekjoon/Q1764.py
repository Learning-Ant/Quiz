'''
자료형 set와 연산자 in을 활용한 판별

좀 더 쉽게 set의 intersection을 활용해 푸는 방법도 가능하다.
set끼리의 intersection은 set의 함수를 사용할 수도 있고,
& 연산자를 통해서도 구할 수 있다.

ex)
set([1, 2, 3]).intersection([2, 3, 4])
{[1, 2, 3]} & {[2, 3, 4]}

40136 KB	124 ms
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

h = [input().strip() for _ in range(n)]
s = set([input().strip() for _ in range(m)])

sh = []

for i in h:
  if i in s:
    sh.append(i)

print(len(sh))
print('\n'.join(sorted(sh)))