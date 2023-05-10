# A와 B를 deque에 넣고
# B를 rotate(1) 해가면서
# a와 b가 같은지 비교하고 같다면 return i
# 모두 확인했는데 같지 않다면 return -1

from collections import deque

def solution(A, B):
    if A == B:
        return 0
    
    a = deque(A)
    b = deque(B)
    for i in range(1, len(a)):
        a.rotate(1)
        if (a == b): return i;
    return -1