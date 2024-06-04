coins = [25, 10, 5, 1]

n = int(input())

for _ in range(n):
    c = int(input())
    result = []
    for coin in coins:
        result.append(c // coin)
        c %= coin
    print(*result)
