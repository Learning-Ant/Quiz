# 도시
# [다음 도시까지의 거리, 유가] -> 마지막 도시는 [0, 유가]
'''
44552 KB	160 ms
'''
import sys
input = sys.stdin.readline
nCity = int(input())

distances = list(map(int, input().split()))
distances.append(0)
prices = list(map(int, input().split()))
cities = list(zip(distances, prices))

minPrice = cities[0][1]
sumPrice = 0
for city in cities:
    if minPrice > city[1]:
        minPrice = city[1]
    sumPrice += (minPrice*city[0])

print(sumPrice)
