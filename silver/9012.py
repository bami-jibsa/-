N = int(input())

for _ in range(N):
    a = str(input())
    for _ in range(len(a)):
        if '()' in a:
            a = a.replace('()', '')
        else:
            break
    if len(a) > 0:
        print('NO')
    else:
        print('YES')