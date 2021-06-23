'''
29200 KB	80 ms
100에 보다 가까울 경우를 구할 때 100보다 큰 수가 더 가까울 경우를 고려할 것
'''

sum = 0
mushrooms = [int(input().strip()) for _ in range(10)]

for i in mushrooms:
    if sum + i > 100:
        if abs(100 - (sum + i)) <= 100 - (sum):
            sum += i
        break
    else:
        sum += i

print(sum)
