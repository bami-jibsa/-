# n = int(input())

# lay = [['*' for j in range(n)]for i in range(n)]

# ls_star = []
# cnt = 0
# for i in range(1, n):
#     for j in range(1, n):# 좌표 지정
#         for k in range(i):
#             for l in range(n): 
#                 if lay[k][l] == '*':
#                     ls_star += k + l# 만들어진애 찾기
#         for m in range(0, len(ls_star), 2):
#             if m + 1 < len(ls_star):
#                 v = m + 1           #만들어진애 가져오기
#                 for _ in range(len(ls_star)):
#                     if any(lay[i][k] == lay[m][v] for ): ##### d여기에요

#                         lay[i][k] == ' '# 가져온 조건에 맞는 애 변환하기
#                         if i == n:
#                             cnt += 1
n = 8

queen_list = []
cnt = 0
def check(queen, new):
    if queen[1] == new[1] or abs(queen[0] - new[0]) == abs(queen[1] - new[1]):
        return False
    return True

    
        

def find_nqueen(x):
    global cnt
    if x == n:
        cnt += 1
        return
    for y in range(n):
        a = True
        for queen in queen_list:
            if not check(queen, (x, y)):
                a = False
                break
        if a:
            queen_list.append((x, y))
            find_nqueen(x + 1)
            queen_list.pop()  

find_nqueen(0)

print(cnt)
  




