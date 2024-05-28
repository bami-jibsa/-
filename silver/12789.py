# import sys
# from collections import deque

# input = sys.stdin.readline

# def sort_check(queue):
#     return queue == sorted(queue)

# def cal():
#     n = int(input())
#     li = deque(map(int, input().split()))
#     stack = []
#     pas_S = []

#     current = 1
#     while li or stack:
#         if li and li[0] == current:
#             pas_S.append(li.popleft())
#             current += 1
#         elif stack and stack[-1] == current:
#             pas_S.append(stack.pop())
#             current += 1
#         elif li:
#             stack.append(li.popleft())
#         else:
#             break

#     if sort_check(pas_S):
#         print("Nice")
#     else:
#         print("Sad")

# cal()
import sys
from collections import deque

input = sys.stdin.readline

def cal():
    n = int(input())
    li = deque(map(int, input().split()))
    stack = []
    current = 1

    while li or stack:
        if li and li[0] == current:
            li.popleft()
            current += 1
        elif stack and stack[-1] == current:
            stack.pop()
            current += 1
        elif li:
            stack.append(li.popleft())
        else:
            break

    if current == n + 1:
        print("Nice")
    else:
        print("Sad")

cal()
