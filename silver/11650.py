import sys

input = sys.stdin.readline

n = int(input())

lay = []

for i in range(n):
    [a, b] = map(int, input().split())
    lay.append([a, b])

s_lay = sorted(lay)

for i in range(n):
    print(s_lay[i][0], s_lay[i][1])