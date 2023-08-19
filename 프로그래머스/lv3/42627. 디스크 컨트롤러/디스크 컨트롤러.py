from collections import deque
import heapq

def solution(jobs):
    # 지금 시점에 시작할 수 있는 작업이 있다면:
    #   지금 시점에 시작할 수 있는 작업 중 가장 빨리 끝나는 것 수행
    # else:
    #   가장 빨리 시작할 수 있는 작업을 수행

    # job = [도착시간, 소요시간]
    length = len(jobs)
    jobs = deque(sorted(jobs, key=lambda x: (x[0], x[1])))
    heap, time, answer = [], 0, 0
    
    while jobs:
        # 수행 가능한 작업을 heap에 넣는다.
        while jobs and jobs[0][0] <= time:
            s, d = jobs.popleft()
            heapq.heappush(heap, (d, s))
        
        if heap:
            # 수행할 수 있는 작업이 있다면
            # 소요시간이 가장 짧은 것을 수행
            d, s = heapq.heappop(heap)
            answer += (time - s) + d
            time += d
        else:
            # 수행할 수 있는 작업이 없다면
            # 가장 빨리 수행할 수 있는 작업을 수행
            if jobs:
                s, d = jobs.popleft()
                answer += d
                time = s+d
    
    while heap:
        d, s = heapq.heappop(heap)
        answer += (time - s) + d
        time += d
        
    return answer // length