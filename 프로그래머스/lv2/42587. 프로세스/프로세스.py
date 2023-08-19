# 1. 대기 큐에서 대기중인 프로세스를 하나 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3-1. 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료합니다.
from collections import deque

def solution(priorities, location):
    answer = 0
    sorted_priorities = sorted(priorities, key=lambda x: x)
    priorities = deque((i, p)for (i, p) in enumerate(priorities))
    
    while priorities:
        i, p = priorities.popleft()
        
        if p == sorted_priorities[-1]:
            sorted_priorities.pop()
            answer += 1
            
            if i == location:
                return answer
        else:
            priorities.append((i, p))
            
    return -1