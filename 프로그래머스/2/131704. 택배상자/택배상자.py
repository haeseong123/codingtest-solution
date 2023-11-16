# 보조 = stack
from collections import deque


def solution(order):
    answer, sub = 0, []
    order = deque(order)
    
    for i in range(1, len(order) + 1):
        if order[0] == i:
            order.popleft()
            answer += 1
            continue
        
        while sub and order and sub[-1] == order[0]:
            order.popleft()
            sub.pop()
            answer += 1
        
        sub.append(i)
            
    while sub:
        if sub[-1] == order[0]:
            order.popleft()
            sub.pop()
            answer += 1
        else:
            break
            
    return answer