# 사원
#   - 근무 태도, 동료 평가

# 한 사원이 다른 사원보다 근태, 동평 점수가 모두 낮다면 그 사람은 인센티브 못 받음
# 그렇지 않은 사원들에 대해서는 두 점수의 합이 높은 순으로 석차를 내어 석차에 따라 인센티브 차등 지급
# 두 점수의 합이 돌일하면 동석차이며, 동석차의 수만큼 다음 석차는 건너 뜀
# e.g., 1등이 2명이면 그 다음등수는 3등부터

# 완호의 석차를 return해 주세요

# 합이 동률이면 거기서 멈추고
# 낮으면 계속 찿ㅈ고
# 마지막에 인센티브 지급 여부를 확인해야 하는데

def solution(scores):
    wanho, wanho_sum = scores[0], sum(scores[0])
    max_s, answer = 0, 1
    for s in sorted(scores, key=lambda x: (-x[0], x[1])):
        if wanho[0] < s[0] and wanho[1] < s[1]:
            return -1
        
        if max_s <= s[1]:
            if wanho_sum < s[0] + s[1]:
                answer += 1
            max_s = s[1]
    return answer