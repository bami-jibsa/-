from collections import deque

M, N = map(int, input().split())
layer = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if layer[i][j] == 1:
                queue.append((i, j, 0))

    while queue:
        x, y, day = queue.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and layer[nx][ny] == 0:
                layer[nx][ny] = 1
                queue.append((nx, ny, day + 1))

    for i in range(N):
        for j in range(M):
            if layer[i][j] == 0:
                return -1
    return day

result = bfs()
print(result)
