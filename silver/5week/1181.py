n = int(input())
Ls = []
for _ in range(n):
    Ls.append(input())

Ls.sort()
Ls.sort(key=len)
for i in Ls:
    print(i)      