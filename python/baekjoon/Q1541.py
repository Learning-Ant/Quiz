'''
29200 KB	76 ms
'''

import sys
input = sys.stdin.readline


calcul = input().strip().split('-')
for i in range(len(calcul)):
    calcul[i] = list(map(int, calcul[i].split('+')))

# print(calcul)
result = sum(calcul[0])

for i in range(1, len(calcul)):
    result -= sum(calcul[i])
print(result)
