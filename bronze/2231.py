import sys 
input = sys.stdin.readline

def sum(n):
    for i in range(1, n + 1):
        a = i + sum(map(int, str(i)))
        if a == n:
            return i
    return 0  

N = int(input().strip())

result = sum(N)

print(result)
        
        
    