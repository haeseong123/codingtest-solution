def solution(k, d):
    answer = 0
    d2 = d * d
    for x in range(0, d + 1, k):
        x2 = x * x
        answer += (((d2 - x2)**0.5) // k) + 1
    return answer