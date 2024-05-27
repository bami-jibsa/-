n = int(input())

lay = [0] * (n + 1)

for i in range(2, n + 1):

    lay[i] = lay[i - 1] + 1

    if i % 2 == 0:
        lay[i] = min(lay[i], lay[i // 2] + 1)

    
    if i % 3 == 0:
        lay[i] = min(lay[i], lay[i // 3] + 1)

print(lay[n])
