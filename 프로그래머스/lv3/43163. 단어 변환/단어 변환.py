# <문제 설명>
# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 
# 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.

# 예를 들어 begin이 "hit", target가 "cog", 
# words가 ["hot","dot","dog","lot","log","cog"]라면 
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 
# 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

# <제한사항>
# 각 단어는 알파벳 소문자로만 이루어져 있습니다.
# 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
# words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
# begin과 target은 같지 않습니다.
# 변환할 수 없는 경우에는 0를 return 합니다.

# <문제 풀이>
# 한 단어에서 다른 단어로 갈 수 있다는 것은 A 단어에서 B 단어로 갈 수 있는 간선이 있다는 말과 같습니다.
# 따라서 words는 그래프로 표현할 수 있습니다.
# 정리하면 위의 예를 들어 "hit" -> "cog"로 가는 최단 거리를 구하는 문제입니다.
# 한 번 이동할 때마다 1만큼 cnt++이 되므로(가중치가 없으므로) bfs를 사용하여 문제를 풀 수 있습니다.
# graph는 hash map을 사용하여 인접 리스트로 표현합니다.
# 예를 들면 아래와 같습니다.
# { "hit": {"hot"}, "hot": {"dot", "lot"}, ... }

# 0. target이 words에 있는지 확인합니다.
# 1. words를 순회하며 graph를 만듭니다.
# 2. graph[begin]부터 시작하여 target까지 도착하는 거리를 구하는 bfs()를 실행합니다.
from collections import deque


def is_neighbor(w1, w2):
    diff = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            diff += 1
            if diff >= 2:
                return False
    return True


def solution(begin, target, words):
    def bfs():
        visited = set()
        visited.add(begin)
        que = deque()
        que.append((begin, 0))

        while que:
            curr, cnt = que.pop()
            
            if curr == target:
                return cnt

            for neighbor in graph[curr]:
                if neighbor in visited:
                    continue
                que.append((neighbor, cnt + 1))
                visited.add(neighbor)

        return 0

    words.append(begin)
    graph = {}
    for i, word in enumerate(words):
        graph[word] = set()
        for neighbor in words:
            if word != neighbor and is_neighbor(word, neighbor):
                graph[word].add(neighbor)
                
    return bfs()