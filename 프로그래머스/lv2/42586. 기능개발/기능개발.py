# 진행률, 속도
# 1. 진행률 += 속도
# 2. check 진행률 >= 100:
#       tmp = 0
#       while progresses[cursor] >= 100:
#           cursor += 1
#           tmp += 1
#       answer.append(tmp)
def solution(progresses, speeds):
    answer = []
    cursor = 0
    while cursor < len(progresses):
        for i, s in enumerate(speeds):
            progresses[i] += s
            
        if progresses[cursor] < 100:
            continue
        
        tmp = 0
        while cursor < len(progresses) and progresses[cursor] >= 100:
            cursor += 1
            tmp += 1
        answer.append(tmp)
    
    return answer