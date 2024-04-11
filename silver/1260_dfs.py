from collections import deque

N, M, V =  map(int, input().split())

graph = [ [False]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


dfs_visit = []
bfs_visit = []

def dfs(graph, start_node):
    #O가 안간거 X가 간거
    X, O = list(), list()
    X.append(start_node)

    while X:
        node = X[0]
        del X[0]

        if node not in O:
            O.append(node)
            connected = []
            global N
            global graph
            for i in range(1, N - 1):
                if graph[node][i] == True:
                    X.append(i)
    return dfs_visit.extend(O)



#아직 BFS안함
#이거랑 비슷하게 가면 될듯?
#내가 맞다면 말이지...
        



print(graph)