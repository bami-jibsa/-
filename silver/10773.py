N = int(input())
b = []
for _ in range(N):
    a = int(input())
    if a == 0:
        b.pop()
    else:
        b.append(a)
c = sum(b)
print(c)