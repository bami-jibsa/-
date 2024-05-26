N, M = map(int, input().split())

lay = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if lay[i][j] == 1:
            homes.append((i, j))
        elif lay[i][j] == 2:
            chickens.append((i, j))
