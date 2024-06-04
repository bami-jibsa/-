def cal(a):
    big = []
    for i in a:
        if i in '([':
            big.append(i)
        elif i == ')':
            if not big or big[-1] != '(':
                return False
            big.pop()
        elif i == ']':
            if not big or big[-1] != '[':
                return False
            big.pop()
    return not big

while True:
    li = input().rstrip() 
    if li == '.':
        break
    print("yes" if cal(li) else 'no')
