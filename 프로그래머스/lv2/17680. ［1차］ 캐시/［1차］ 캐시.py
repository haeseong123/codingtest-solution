# LRU
# cache hit
#   > 실행시간 +1
#   > 해당 값 지우고
#   > 다시 넣기
# cache miss
#   > 실행시간 +5
#   > 값 삭제하고 pop(0)
#   > 이번 값 추가 append(value)
from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    que = deque()
    answer = 0

    for c in cities:
        city = c.lower()
        if city in que:
            answer += 1
            que.remove(city)
            que.append(city)
        else:
            answer += 5
            if len(que) == cacheSize:
                que.popleft()
            que.append(city)

    return answer
