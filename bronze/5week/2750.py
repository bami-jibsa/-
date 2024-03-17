n = int(input())
ls = []
for _ in range(n):
    ls += list(map(int, input()))

for i in range(1, len(ls)):
    for j in range(i, 0, -1):
        if ls[j-1] > ls[j]:
            ls[j-1], ls[j] = ls[j], ls[j-1]    
            
for _ in range(len(ls)):
    print(ls.pop())