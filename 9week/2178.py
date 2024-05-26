# n, k = map(int, input().split())

# layer = [list(map(int, input().strip())) for _ in range(n)]


# def dp(n, k):
#     for i in range(k):

n, k = map(int, input().split())
layer = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    stack = [(x, y)]
    layer[x][y] = 1

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < k and layer[nx][ny] == 1:
                stack.append((nx, ny))
                layer[nx][ny] = layer[x][y] + 1

dfs(0, 0)
print(layer[n-1][k-1])


