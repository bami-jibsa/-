import sys
N = int(input())

num = list(map(int, input().split()))

ops = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9 

def btr(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    if plus:
        btr(depth + 1,total + num[depth], plus - 1, minus, multiply, divide)
    
    if plus:
        btr(depth + 1,total - num[depth], plus, minus - 1, multiply, divide)
    if plus:
        btr(depth + 1,total + num[depth], plus, minus, multiply - 1, divide)
    if plus:
        btr(depth + 1,int(total) / num[depth], plus, minus, multiply, divide - 1)

btr(1, num[0], ops[0], ops[1], ops[2], ops[3])
print(maximum)
print(minimum)




