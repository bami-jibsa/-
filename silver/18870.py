import sys
input = sys.stdin.readline
N = int(input())
li = list(map(int, input().rstrip().split()))

s_li = sorted(list(set(li)))
list_dict = dict(zip(s_li, list(range(len(s_li)))))

for x in li:
    print(list_dict[x])

