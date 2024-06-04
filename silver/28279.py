import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
li = deque()

def cal(x):
    if x[0] == 1:
        li.appendleft(x[1])
    elif x[0] == 2:
        li.append(x[1])
    elif x[0] == 3:
        if li:
            print(li.popleft())
        else:
            print(-1)
    elif x[0] == 4:
        if li:
            print(li.pop())
        else:
            print(-1)
    elif x[0] == 5:
        print(len(li))
    elif x[0] == 6:
        if li:
            print(0)
        else:
            print(1)
    elif x[0] == 7:
        if li: 
            print(li[0])
        else:
            print(-1)
    elif x[0] == 8:
        if li:
            print(li[-1])
        else:
            print(-1)

for _ in range(n):
    ord = list(map(int, input().strip().split()))
    cal(ord)
