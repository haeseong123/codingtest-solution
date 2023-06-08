# <문제 설명>
# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 
# Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.

# 아래 매개변수가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야하는 최소 횟수를 반환해 주세요.
# scoville: Leo가 가진 음식의 스코빌 지수를 담은 배열
# K: 원하는 스코빌 지수

# <제한 사항>
# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

# <문제 풀이>
# 가장 낮은 우선순위를 갖는 원소 두 개를 뽑아야 하므로 heap을 사용하면 좋을 듯하다.
# scoville의 모든 원소를 최소힙에 넣고
# 최솟값이 K이상이 될때까지 "특별한 방법"으로 조합을 하면 된다.
# 단, 최소힙의 원소가 하나 있는데, 그 값이 K 미만이라면 -1을 반환해야 한다.
import heapq

def solution(scoville, K):
    answer, heap = 0, []
    for s in scoville:
        heapq.heappush(heap, s)
    
    while heap:
        min1 = heapq.heappop(heap)
        if min1 >= K:
            return answer
        if not heap:
            break
        
        min2 = heapq.heappop(heap)
        heapq.heappush(heap, min1 + (min2 << 1))
        answer += 1
    
    return -1
    
    
    