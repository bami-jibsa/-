n = [int(input()) for _ in range(5)]
a = sum(n) // len(n)
n.sort()
m = n[len(n) // 2]
print(a)
print(m)
