# n^2는 너무 비싸고
# enemy를 한 번 도는 것은 무조건 필요
# 더이상 진행이 불가능할 때 가장 컷던 enermy를 '무적권'으로 막는 전략
# enermy를 삽입하고 삭제하는 기능이 필요하므로 최대힙이 필요
# 힙은 삽입 삭제가 logN이므로
# 총 O(N + logN)
import heapq


def solution(n, k, enemy):
    heap = []
    answer = 0

    for e in enemy:
        n -= e
        heapq.heappush(heap, -e)

        if n < 0 and k > 0:
            n -= heapq.heappop(heap)
            k -= 1

        if n < 0:
            break

        answer += 1

    return answer
