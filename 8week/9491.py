import sys
input = sys.stdin.readline

T = int(input())

def pec():
    n = int(input())
    dp = [None] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
    # print(i)
        dp[i] = (dp[i - 3] + dp[i -2]) 
    print(dp[n - 1])
    # print(dp[i])
# 3 2
# 4 2
# 5 3
for _ in range(T):
    pec()

