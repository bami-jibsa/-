import sys

input = sys.stdin.readline

li = []
for _ in range(5):
    li += list(map(str, input().split()))

for i in range(15):
    for j in range(15):
        try:
            print(li[j][i], end='')
        except:IndexError


## 1 2 3 
#1 a b c
#2 d e f
#3 g h k