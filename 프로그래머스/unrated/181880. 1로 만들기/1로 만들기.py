def solution(num_list):
    answer = 0
    for num in num_list:
        cnt = 0
        while num > 1:
            cnt += 1
            num >>= 1
        answer += cnt
    return answer