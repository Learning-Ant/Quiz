'''
    처음 visited를 list형식으로 각 정점에 대한 방문여부를 bool의 형태로 저장했었다.
    하지만 이는 BOJ에서 시관초과를 발생시켰다.
    이 visited를 set로 바꿔 방문한 정점을 여기에 저장시키고, set안에 해당 정점이 포함되어 있는지를
    판단하는 것으로 바꾸니 무리없이 '맞았습니다'를 얻을 수 있었다.
    기억해두자.
'''

from collections import deque
import sys

input = sys.stdin.readline

v, eCount = map(int, input().strip().split())
graph = [[] for _ in range(v + 1)]
for _ in range(eCount):
    edge = list(map(int, input().strip().split()))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

# visited = [False] * (v + 1)
visited = set()

queue = deque()
comCount = 0
# conCom = []
for i in range(1, v+1):
    #print("---", i, "번째---")
    if i in visited:
        continue
    queue.append(i)
    visited.add(i)
    # component = [i]
    while queue:
        cur = queue.popleft()
        # print("---현재 node : ", cur, "---")
        # visited[cur] = True
        # print(visited)
        # print(graph[cur])
        for j in graph[cur]:
            # print(j)
            # if not visited[j]:
            if j not in visited:
                #print("---연결 node({}) 추가---".format(j))
                visited.add(j)
                queue.append(j)
                # component.append(j)
        # conCom.append(component)
    comCount += 1

# for i in graph:
#     print(i)

# for i in conCom:
#     print(i)

# print(len(conCom))
sys.stdout.write(str(comCount))
