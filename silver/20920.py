import sys

input = sys.stdin.readline
n, m = map(int, input().split())

note = dict()

for _ in range(n):
    s = input().strip()
    if len(s) >= m:
        if s in note:
            note[s] += 1
        else:
            note[s] = 1
note = sorted(note.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))
for i in note:
    print(i[0])