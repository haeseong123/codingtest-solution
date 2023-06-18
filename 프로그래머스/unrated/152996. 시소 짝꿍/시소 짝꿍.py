# <문제 설명>
# 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면 시소 짝꿍
# 사람들의 몸무게 목록 weights이 주어질 때, 
# 시소 짝꿍이 몇 쌍 존재하는지 구하여 
# return 하도록 solution 함수를 완성해주세요.

# <제한사항>
# 2 ≤ weights의 길이 ≤ 100,000
# 100 ≤ weights[i] ≤ 1,000
#   몸무게 단위는 N(뉴턴)으로 주어집니다.
#   몸무게는 모두 정수입니다.

# <문제 풀이>
# 무게가 같다면 짝꿍
# 무게가 다르다면
#   (2, 3), (2, 4), (3, 4)
#   x가 큰거 y가 작은 거일 때
#   x = 3/2y
#   x = 2y
#   x = 4/3y
#   에 속하면 answer += 1
# brute force로 풀면 O(N^2)
#   => 시간 초과
# 어떻게 시간을 줄일 수 있을까?
# 지금 어떤 계산을 중복으로 하고있을까?
# weights를 해시셋으로 만들고 weights를 순회하며 in 을 사용하면 O(N)에 실행가능하다.
# 하지만 동일값(100, 100)이 있을 수 있으니 해당 경우를 먼저 처리한 후
# set을 사용하여 풀이하자
# 동일 값의 갯수를 C(n, 2) 하면 그것이 동일 값의 짝꿍 갯수이다.
from collections import Counter

def solution(weights):
    answer = 0
    
    counter = Counter(weights)
    for count in counter.values():
        if 2 <= count:
            answer += (count * (count - 1)) // 2
    
    weights = set(weights)
    for w in weights:
        if w*3/2 in weights: 
            answer += counter[w] * counter[w*3/2]
        if w*2 in weights:
            answer += counter[w] * counter[w*2]
        if w*4/3 in weights:
            answer += counter[w] * counter[w*4/3]
            
    return answer