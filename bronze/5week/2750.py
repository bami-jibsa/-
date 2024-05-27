n = int(input())
ls = [int(input()) for _ in range(n)]

for i in range(len(ls)):
    for j in range(1, len(ls) - i):
        if ls[j-1] > ls[j]:
            ls[j-1], ls[j] = ls[j], ls[j-1]

for num in ls:
    print(num)
