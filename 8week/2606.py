n = int(input())
m = int(input())

graph = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    
visit = []

def dfs(graph, start_node):
    visit.append(start_node)
    for i in range(1, n + 1):
        if graph[start_node][i] and i not in visit:
            dfs(graph, i)
            
dfs(graph, 1)

print(len(visit) - 1)