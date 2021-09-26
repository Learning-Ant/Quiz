'''
이 전에 풀었던 집중국 문제와 같은 유형의 문제

62820 KB	312 ms
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

costs = list(map(int, input().strip().split()))
diff = sorted([costs[i] - costs[i-1] for i in range(1, n)], reverse=True)

print(sum(diff[k-1:]))