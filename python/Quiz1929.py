import sys
import math

input = sys.stdin.readline

begin, end = map(int, input().strip().split())

for i in range(begin, end + 1):
    flag = True
    if i == 1:
        continue
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)

# 위와 같이 제곱근을 이용해서 구할 수도 있다. (5~6초)
# 하지만 이는 에라토스테네스의 체보다 훨씬 많은 시간을 소요한다. (1초 이하)
