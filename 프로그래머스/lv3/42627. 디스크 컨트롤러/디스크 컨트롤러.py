# 현재 실행할 수 있는 작업 중 끝나는 시간이 제일 빠른 것 먼저 뽑아서
# 실행하고, 해당 작업이 요청 된 시점부터 종료된 시간까지의 길이를 계산하여 누적하고
# 해당 누적값 // len(jobs)를 반환하자.

import heapq

def solution(jobs):
    length = len(jobs)
    acc, now = 0, 0
    heap = []
    
    while jobs:
        for i, j in enumerate(jobs):
            if j[0] <= now:
                heapq.heappush(heap, [j[1], j[0], i])
        
        if heap:
            # 소요 시간, 도착 시간
            need, arrival, i = heapq.heappop(heap)
            now += need
            acc += now - arrival
            jobs.pop(i)
        else:
            now += 1
        heap = []
    
    return acc // length    