from queue import Queue

n = int(input())

layer = [['*' for _ in range(n)] for _ in range(n)]


for i in range(n):
    li = []
    li += input().split()
    for j in range(n):
        layer[i][j] = li[j]


def cal(name, x):
    sco = 0
    for i in range(len(name)):
        for j in range(i + 1, len(name)):
            sco += int(x[name[i]][name[j]]) + int(x[name[i]][name[j]])
    return sco

def back(n, z):
    min_ = float('inf')
    queue = Queue()
    queue.put((0, [], []))

    while not queue.empty():
        idx, team_s, team_l = queue.get()

        if idx == n:
            if len(team_s) == n // 2 and len(team_l) == n // 2:
                s_sco = cal(team_s, z)
                l_sco = cal(team_l, z) 
                min_ = min(min_, abs(s_sco - l_sco))
            continue

        if len(team_s) < n // 2:
            queue.put((idx + 1, team_s + [idx], team_l))

        if len(team_l) < n // 2:
            queue.put((idx +  1, team_s, team_l + [idx]))
    return min_

print(back(n, layer))



