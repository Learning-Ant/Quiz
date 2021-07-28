'''
* sorted의 key 속성으로 다중 조건 정렬
34500 KB	124 ms
'''

import sys

input = sys.stdin.readline

n = int(input())

vocaList = sorted(list(set([input().strip()
                  for _ in range(n)])), key=lambda x: (len(x), x))
print('\n'.join(vocaList))
