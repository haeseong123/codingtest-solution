import heapq

def solution(scoville, K):
    # 섞은 음식의 스코빌 지수 = 
    #   가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    count = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        if scoville[0] >= K:
            return count
        
        m1 = heapq.heappop(scoville)
        m2 = heapq.heappop(scoville)
        heapq.heappush(scoville, m1 + (m2 << 1))
        count += 1
    
    return -1 if scoville[0] < K else count
