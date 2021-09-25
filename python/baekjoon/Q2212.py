'''
포인트는 구간 나누기를 코드로 어떻게 녹여내야할 지 이다.

집중국이 전담할 구간을 나눈다 = 수신기 간 거리 중 하나는 무시 가능하다
그러므로 집중국의 개수 - 1 만큼 수신기의 거리를 무시할 수 있게된다.
이를 각 수신기간의 거리의 차이를 구하고 가장 큰 거리들을 집중국의 개수 - 1개만큼 제외해주는
방법으로 구현하는 것이다.

30220 KB	80 ms
'''

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
ls = sorted(list(map(int, input().strip().split())))
diff = sorted([ls[i] - ls[i-1] for i in range(1, n)], reverse=True)

print(sum(diff[k-1:]))