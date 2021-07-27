'''
29200 KB    72 ms
'''

import sys
input = sys.stdin.readline


def check(voca: str) -> bool:
    if len(voca) < 3:
        return True
    else:
        chkSet = set()
        chkSet.add(voca[0])
        p = voca[0]
        for i in voca:
            # print(chkSet)
            if p != i:
                p = i
                if i not in chkSet:
                    chkSet.add(i)
                else:
                    return False

    return True


tc = int(input())

result = 0
for _ in range(tc):
    if check(input().strip()):
        result += 1

print(result)
