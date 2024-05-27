n = int(input())

a = 0

def cal(num):
    return '666' in str(num)
cnt = 0
while True:
    a += 1
    if cal(a) == True:
        cnt += 1
    if cnt == n:
        break
        
print(a)
