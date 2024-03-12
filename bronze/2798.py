# import sys
# input = sys.stdin.readline
# a, b = map(int, input().split())

# ls = list(map(int, input().split()))
# Ls = []
# #set 써서 정렬하기 b 뻬서 얼마나 가까운지 구하기
# y = 1000

# for i in ls:
#     for j in ls:
#         for k in ls:
#             if len({i, j, k}) == 3:
#                 x = i + j + k
#                 z = abs(x - b)
#                 if y > z:
#                     y = x



# print(y)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i] + arr[j] + arr[k] > M:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])
print(result)