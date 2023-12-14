def solution(n):
    answer = 0
    for i in range(1, n + 1):
        acc = 0
        for j in range(i, n + 1):
            acc += j
            
            if acc == n:
                answer += 1
                break
            
            if acc > n:
                break
    return answer