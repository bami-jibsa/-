#가로 함수
#세로 함수
#9칸 함수 -- 
#a b c
#d e f
#g h i


import sys

input = sys.stdin.readline()

lay = []
for _ in range(9):
    rw = list(map(int, input().split()))
    lay.append(rw) 
 
cells  = [[2, 2], [2, 5], [2, 8], 
          [5, 2], [5, 5], [5, 8], 
          [8, 2], [8, 5], [8, 8]]

def row(n, num1):
    if n in lay[num1]:
        return False
    else :
        return True
def col(n, num2):
    for i in range(9):
        if n in lay[i][num2]:
            return False
        else:
            return True
        
def inx_cel(a, b):
    if a < 2 and b < 2:
        return 1
    elif a < 2 and b < 5:
        return 2
    elif a < 2 and b < 8:
        return 3
    elif a < 5 and b < 2:
        return 4
    elif a < 5 and b < 5:
        return 5
    elif a < 5 and b < 8:
        return 6
    elif a < 8 and b < 2:
        return 7
    elif a < 8 and b < 5:
        return 8
    elif a < 8 and b < 8:
        return 9
    
mov_X = [0, -1, 1]
mov_y = [-1, 1, 0]

idx_num = {1:[1, 1], 2:[1, 4], 3:[1, 7],
           4:[4, 1], 5:[4, 4], 6:[4, 7],
           7:[7, 1], 8:[7, 4], 9:[7, 7]}

def cells(n, inx):
    value = idx_num[inx]
    li = []
    for i in mov_X:
        for j in mov_y:
            li.append(lay[value[0] + i][value[1] + j])

    if n in li:
        return False
    elif n not in li:
        return True

def end_war():
    for i in range(9):
        for j in range(9):
            if lay[i][j] == 0:
                row(lay[i][j], i)
                col(lay[i][j], j)
                inx = inx_cel(i, j)
                cells(lay[i][j], inx)




    