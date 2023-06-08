# <문제 설명>
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다.
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# 아래 매개변수가 주어질 때, 완주하지 못한 선수의 이름을 반환해주세요.
# participant: 마라톤에 참여한 선수들의 이름이 담긴 배열
# completion: 완주한 선수들의 이름이 담긴 배열

# <제한사항>
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.

# <풀이>
# 동명이인이 있을 수 있으므로, 단순히 dict(boolean) 으로 해시를 만들면 안 되고
# 다른 방법을 강구해야 한다.
# 1. participant를 순회하며 아래를 수행한다.
#   1-1. key는 hash(p) value는 p로 dict를 만든다.
#   1-2. hash_sum에 hash(p) 값을 더한다.
# 2. completion을 순회하며 아래를 수행한다.
#   2-1. hash_sum에 hash(c) 값을 뺀다.
# 3. dict[hash_sum] 을 반환한다.
def solution(participant, completion):
    hash_map = {}
    hash_sum = 0
    
    for p in participant:
        hash_map[hash(p)] = p
        hash_sum += hash(p)

    for c in completion:
        hash_sum -= hash(c)
        
    return hash_map[hash_sum]