import sys 
input = sys.stdin.readline

layer = []
for i in range(9):
    layer.append(list(map(int, input().split())))

max_ = max(max(i) for i in layer)

for i in range(len(layer)):
    for j in range(len(layer[i])):
        if layer[i][j] == max_:
            print(max_)
            print(i + 1, j + 1)
