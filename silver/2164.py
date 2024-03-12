import sys 
from collections import deque
input = sys.stdin.readline
N = int(input())
a = deque([i for i in range(1, N + 1)])

while len(a) >= 1:
    if len(a) == 1:
        print(a.pop())
        break
    a.popleft()
    b = a.popleft()
    a.append(b)