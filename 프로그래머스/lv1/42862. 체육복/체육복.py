# <문제 설명>
# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 
# 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
# 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
# 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
# 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

# 아래 매개변수가 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 반환해 주세요.
# n: 전체 학생의 수
# lost: 체육복을 도난당한 학생들의 번호가 담긴 배열
# reserve: 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열

# <제한사항>
# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

# <문제 풀이>
# 결국 n - len(lost) 하면 그게 답인데
# lost를 어떻게 줄여나갈 것인가?
# lost를 모두 set에
# reserve를 순회하며 아래를 수행한다.
#       if set in e: -> set.remove(e)
#       elif set in e - 1: -> set.remove(e - 1)
#       elif set in e + 1: -> set.remove(e + 1)
# return n - len(set)
def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    common_set = lost_set & reserve_set
    lost_set -= common_set
    reserve_set -= common_set
    
    for r in sorted(list(reserve_set)):
        if r in lost_set:
            lost_set.remove(r)
        elif r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)
            
    return n - len(lost_set)