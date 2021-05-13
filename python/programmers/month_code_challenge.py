def query1(values, edges, start):
    visit = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            for i in edges:
                if i[0] == node:
                    stack.append(i[1])
    _sum = 0

    for i in visit:
        _sum += values[i - 1]

    return _sum


def query2(values, edges, node, w):
    if node == 1:
        values[node - 1] = w
        return
    else:
        for edge in edges:
            if edge[1] == node:
                values[node - 1] = values[edge[0] - 1]
                query2(values, edges, edge[0], w)


def solution(values, edges, queries):
    answer = []

    for query in queries:
        if(query[1] == -1):
            answer.append(query1(values, edges, query[0]))
        else:
            query2(values, edges, query[0], query[1])

    return answer
