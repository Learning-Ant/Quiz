import sys
input = sys.stdin.readline
n = int(input().strip())
_list = [int(input().strip()) for _ in range(n)]

_list.sort()

print('\n'.join(map(str, _list)))
