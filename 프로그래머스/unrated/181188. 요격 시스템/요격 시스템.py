# 1. targets를 끝점 기준 내림차순으로 정렬합니다.
# 2. targets이 텅 빌때 까지 아래를 반복합니다.
# 3.     answer += 1를 합니다.
# 4.    targets에서 마지막 요소를 뽑습니다.
# 5.    해당 요소의 끝점을 포함하는 모든 targets를 pop() 합니다.
# 6. answer를 반환합니다.
def solution(targets):
    answer = 0
    targets.sort(key=lambda x: -x[1])
    
    while targets:
        answer += 1
        start, end = targets.pop()
        while targets and (targets[-1][0] < end):
            targets.pop()
            
    return answer