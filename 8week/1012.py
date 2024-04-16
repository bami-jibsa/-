T = int(input())

def check():
    M, N, K = map(int, input().split())

    graph = [[False] * (M) for _ in range(N)]

    not_visit = []
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = True
        graph[b][a] = True
        not_visit.append(a)
        not_visit.append(b)
    not_visit = set(not_visit)
    
    visit = []
    while not_visit:
        def dfs(graph, start_node):
            visit.append(start_node)
            not_visit.remove(start_node)
            
            i = 0
            while True:
                i += 1
                if graph[start_node][i] and i not in visit:
                    
                    continue
                dfs(graph, i)   
        dfs(graph, not_visit[0])

for _ in range(T):
    check()
