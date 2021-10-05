import sys
input = sys.stdin.readline

n, m = map(int, input().split())

h = [input().strip() for _ in range(n)]
s = [input().strip() for _ in range(m)]

sh = []

for i in h:
  if s.count(i) == 1:
    sh.append(i)

print(len(sh))
print('\n'.join(sorted(sh)))