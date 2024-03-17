import sys
import math
input = sys.stdin.readline 

n = int(input())

# layer = [['*' for j in range(n)]for i in range(n)]


# def rout(N, n):
    
#     if N == 1:
#         n = 0
#         return n 
#     n += 1
#     return rout(N/3, n)
# div = rout(n, 0)
# for i in range(int(n/3)):
#     z = 1 + (3 * i)
#     for j in range(int(n/3)):
#         x = 1 + (3 *j)
#         layer[z][x] = ' '

# # if n >= 9:
# #     for i in range(int(n))
# for i in range(n):
#     print()
#     for j in range(n):
#         print(layer[i][j], end='')

# for i in range(3**(div - 1)):
#     for j in range(3**(div - 1)):

# _________________________________________________________
layer = [['*' for _ in range(n)]for _ in range(n)]

def star(lay, n):
    a = int(n/3)
    b = math.log(n, 3)
    if n == 1:
        return 1
    for i in range(b):
        z = a + (3 * i)
        for j in range(b):
            x = a + (3 *j)
            for k in range(a):
                for l in range(a):
                    lay[z + k][x + l] = ' '
    
    return star(lay, n/3) * int(b)
    
    
a = star(layer, n)
print(a)

