import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 트리구조 형성 단일구조 선형구조로

li = list(range(1, n + 1))

def back(li, m):
    if m == 0:
        return
    
