from collections import deque
import heapq


def solution(k, n, reqs):
    # 1. 초기화
    mentors = [[] for _ in range(k)]
    ps_arr = [deque() for _ in range(k)]

    for arrival, needed, index in reqs:
        ps_arr[index - 1].append((arrival, needed))

    for index, ps in enumerate(ps_arr):
        mentor = 0
        if ps:
            arrival, needed = ps.popleft()
            mentor = arrival + needed
        mentors[index].append(mentor)
        n -= 1

    # 2. 계산
    for _ in range(n):
        waiting_times = get_waiting_times(ps_arr, mentors)
        # 대기 시간이 제일 긴 것을 삭제하는 것이 아니라 가장 많이 줄어드는 것을 삭제해야 합니다.
        index = get_max_diff_index(waiting_times, ps_arr, mentors)

        heapq.heappush(mentors[index], sum(ps_arr[index].popleft()))

    waiting_times = get_waiting_times(ps_arr, mentors)
    return sum(waiting_times)


def get_waiting_times(ps_arr, mentors):
    mentors = [m.copy() for m in mentors]
    waiting_times = []
    for (ps, mentor) in zip(ps_arr, mentors):
        time = get_waiting_time(ps, mentor)
        waiting_times.append(time)

    return waiting_times


def get_waiting_time(ps, mentor):
    mentor = mentor.copy()
    time = 0
    for arrival, needed in ps:
        mentor_time = heapq.heappop(mentor)
        if arrival >= mentor_time:
            # 대기 시간 없음
            # mentor_time = 도착 시간 + 걸리는 시간
            mentor_time = arrival + needed
        else:
            # 대기 시간 = mentor_time - 도착 시간
            # mentor_time = mentor_time + 걸리는 시간
            time += mentor_time - arrival
            mentor_time += needed
        heapq.heappush(mentor, mentor_time)
    return time


def get_max_index(arr):
    max_value, max_index = 0, -1
    for index, value in enumerate(arr):
        if max_value < value:
            max_value = value
            max_index = index
    return max_index


def get_max_diff_index(waiting_times, ps_arr, mentors):
    max_diff, max_index = -1, -1

    for index, (waiting_time, ps, mentor) in enumerate(zip(waiting_times, ps_arr, mentors)):
        if not ps:
            continue
            
        ps = ps.copy()
        mentor = mentor.copy()
        heapq.heappush(mentor, sum(ps.popleft()))

        diff = waiting_time - get_waiting_time(ps, mentor)
        if diff > max_diff:
            max_diff = diff
            max_index = index

    return max_index


# 테스트
print(solution(3, 5,
               [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1],
                [70, 100, 2]])
      )
print(solution(2, 3,
               [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]])
      )
print(solution(2, 2,
               [[5, 55, 1], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]])
      )
