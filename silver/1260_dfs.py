from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

dfs_visit = []
bfs_visit = []

def bfs(graph, start_node):
    global N
    X, O = deque(), []
    X.append(start_node)

    while X:
        node = X.popleft()  

        if node not in O:
            O.append(node)
            for i in range(1, N + 1):  
                if graph[node][i]:
                    X.append(i)
    bfs_visit.extend(O)  

def dfs(graph, start_node):
    X, O = [], []
    X.append(start_node)

    while X:
        node = X.pop()

        if node not in O:
            O.append(node)
            for j in range(1, N + 1):  
                if graph[node][j]:
                    X.append(j)
    dfs_visit.extend(O)  

dfs(graph, V)
bfs(graph, V)

print(str(dfs_visit) + ' ' + str(bfs_visit))