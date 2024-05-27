n = int(input())

for i in range(n // 5, -1, -1):
    remainder = n - (5 * i)
    if remainder % 3 == 0:
        print(i + (remainder // 3))
        break
else:
    print(-1)
