n = int(input())
ls = list(map(int, input().split()))

ls.sort()

print(ls[-1] + ls[-2])