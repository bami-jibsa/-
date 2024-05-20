def max_(n, score):
    if n == 1:
        return score[0]
    
    elif n == 2:
        return score[0] + score[1]
    
    lay = [0] * n
    lay[0] = score[0]
    lay[1] = score[0] + score[1]
    lay[2] = max(score[0] + score[2], score[1] + score[2])
    
    for i in range(3, n):
        lay[i] = max(lay[i - 2] + score[i], lay[i - 3] + score[i - 1] + score[i])
    
    return lay[-1]

n = int(input())
score = [int(input()) for _ in range(n)]

print(max_(n, score))
