# import sys
# import math
# input = sys.stdin.readline 

# n = int(input())

# layer = [['*' for _ in range(n)]for _ in range(n)]

# def star(lay, n):
#     a = int(n/3)
#     b = math.log(n, 3)
#     if n == 1:
#         return 1
#     for i in range(b):
#         z = a + (3 * i)
#         for j in range(b):
#             x = a + (3 *j)
#             for k in range(a):
#                 for l in range(a):
#                     lay[z + k][x + l] = ' '
    
#     return star(lay, n/3) * int(b)
    
    
# a = star(layer, n)
# print(a)



import sys

input = sys.stdin.readline

n = int(input().strip())

def star(ll):
    if ll == 1:
        return ['*']
    
    stars = star(ll//3)
    li = []

    for i in stars:
        li.append(i*3)
    for i in stars:
        li.append(i + ' '*(ll//3)+i)
    for i in stars:
        li.append(i*3)
    return li

print('\n'.join(star(n)))
