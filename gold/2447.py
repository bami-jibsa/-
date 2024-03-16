import sys

input = sys.stdin.readline 

n = int(input())

layer = [['*' for j in range(n)]for i in range(n)]

layer[0][1] = 1
a = 0
def rout(N, n):
    
    if N == 1:
        n = 0
        return n 
    n += 1
    return rout(N/3, n)
div = rout(n, 0)
for i in range(3**(div - 1))