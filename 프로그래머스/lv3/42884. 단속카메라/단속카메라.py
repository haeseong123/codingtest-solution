# 1. 끝점 내림차순 정렬
# 2. routes가 빌때까지 순회
# 3.    answer += 1
# 4.    끝점을 뽑고 해당 끝점을 포함하는 모든 선을 pop()
# 5. answer 반환
def solution(routes):
    cnt, answer = 0, 0
    routes.sort(key=lambda x: -x[1])
    
    while routes:
        start, end = routes.pop()
        answer += 1
        while routes and routes[-1][0] <= end <= routes[-1][1]:
            routes.pop()
        
    
    return answer