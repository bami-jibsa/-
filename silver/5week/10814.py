n = int(input())
Ls = []
for _ in range(n):
    ls = list(map(str , input().split()))
    Ls.append(ls)
    print(Ls)
for i in range(1, len(Ls)):
    for j in range(i, 0, -1):
        if Ls[j-1][0] > Ls[j][0]:
            Ls[j-1], Ls[j] = Ls[j], Ls[j-1]    

for i in range(n):
    print(' '.join(Ls[i]))        