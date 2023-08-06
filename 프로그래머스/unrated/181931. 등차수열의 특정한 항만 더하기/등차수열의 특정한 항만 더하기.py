def solution(a, d, included):
    answer = 0
    for ic in included:
        if ic:
            answer += a
        a += d
    return answer