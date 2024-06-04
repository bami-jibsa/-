import sys  
from collections import deque

input = sys.stdin.readline

n = int(input())

li = list(map(int, input().strip().split()))

class cir:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index % len(self.data)]
    
    def __setitem__(self, index, value):
        self.data[index % len(self.data)] = value

lay = []
for i in range(1, n + 1):
    lay.append(i)

cjr_lay = cir(lay)

ckr_li = cir(li)

def cal(layer, li):
    a = 22
    
