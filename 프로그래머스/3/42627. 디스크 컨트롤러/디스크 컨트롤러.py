from collections import deque
import heapq


def solution(jobs):
    # 지금 시점에 시작할 수 있는 작업이 있다면:
    #   지금 시점에 시작할 수 있는 작업 중 가장 빨리 끝나는 것 수행
    # else:
    #   가장 빨리 시작할 수 있는 작업을 수행

    # job = [도착시간, 소요시간]
    # 도착시간 오름차순, 소요시간 오름차순
    length = len(jobs)
    jobs = deque(sorted(jobs, key=lambda x: (x[0], x[1])))
    heap, time, answer = [], 0, 0

    while jobs:
        # 수행 가능한 작업을 heap에 넣습니다.
        while jobs and jobs[0][0] <= time:
            startTime, duration = jobs.popleft()
            heapq.heappush(heap, (duration, startTime))

        # 수행 가능한 작업이 있다면
        if heap:
            duration, startTime = heapq.heappop(heap)
            answer += (time - startTime) + duration
            time += duration
        # 수행 가능한 작업이 없다면
        else:
            # 가장 빨리 수행할 수 있는 작업을 수행
            if jobs:
                startTime, duration = jobs.popleft()
                answer += duration
                time = startTime + duration

    # heap에 있는 것 다 처리
    while heap:
        duration, startTime = heapq.heappop(heap)
        answer += (time - startTime) + duration
        time += duration

    # 값 return
    return answer // length

