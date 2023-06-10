# <문제 설명>
# n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 
# 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 
# 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

# 노드의 개수 n, 
# 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 
# 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

# <제한사항>
# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

# <문제 풀이>
# 한 점(1번 노드)에서 다른 점으로의 모든 최단 거리를 구하고
# max를 찾은 뒤, 해당 max값을 갖는 원소들의 갯수를 반환하면 됩니다.
# 한 점에서 다른 점으로의 모든 최단 거리를 구하는 알고리즘은 다익스트라, 벨만-포드가 있습니다.
# 혹은 가중치가 모두 1이므로 bfs를 사용해도 됩니다.

# 다익스트라 풀이
# 1번을 제외한 모든 노드의 값을 INF로 설정합니다.
# 최소힙에 1번 노드 값을 넣습니다.
# 아래 과정을 총 n - 1번 수행합니다.
#   최소힙에서 최솟값을 꺼냅니다.
#   해당 노드에서 갈 수 있는 모든 노드를 순회합니다.
#       순회 중인 노드가 가진 값보다 (1번 노드 + 1) 값이 더 작다면 해당 값으로 갱신하고 최소힙에 넣습니다.
# 배열을 순회하며 max를 구하고 max값을 cnt한 뒤 반환합니다.

# 벨만-포드 풀이
# 1번을 제외한 모든 노드의 값을 INF로 설정합니다. 1은 0으로 설정합니다.
# 아래 과정을 총 n - 1번 수행합니다.
#       모든 노드를 순회합니다.
#           해당 노드에서 갈 수 있는 모든 neighbor를 순회합니다.
#               해당 neighbor가 갖고있는 값보다 (현재 노드 + 1) 값이 더 작다면 해당 값으로 갱신합니다.
# 배열을 순회하며 max를 구하고 max값을 cnt한 뒤 반환합니다.

# bfs 풀이
# 1번에서 갈 수 있는 모든 노드를 순회합니다.
#   1번에서 해당 노드까지의 거리를 bfs를 사용하여 계산합니다.
# 배열을 순회하며 max를 구하고 max값을 cnt한 뒤 반환합니다.
import heapq
from collections import deque

graph = []
INF = float("inf")

def count_max_value(arr):
    _max = max(arr)
    count = 0
    for e in arr:
        if e == _max:
            count += 1
    return count
    
def dijkstra():
    global graph
    distances = [INF] * len(graph)
    distances[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))
    
    for _ in range(len(graph) - 2):
        distance, idx = heapq.heappop(heap)
        
        for neighbor in graph[idx]:
            if distances[neighbor] > distance + 1:
                distances[neighbor] = distance + 1
                heapq.heappush(heap, (distance + 1, neighbor))
    
    return count_max_value(distances[1:])

def bellman_ford():
    global graph
    distances = [INF] * len(graph)
    distances[1] = 0
    
    for _ in range(len(graph) - 2):
        for i in range(1, len(graph)):
            for v in graph[i]:
                if distances[v] > distances[i] + 1:
                    distances[v] = distances[i] + 1
                    
    return count_max_value(distances[1:])
    
def bfs():
    
# bfs 풀이
# 1번을 제외한 모든 노드를 순회합니다.
#   1번에서 해당 노드까지의 거리를 bfs를 사용하여 계산합니다.
# 배열을 순회하며 max를 구하고 max값을 cnt한 뒤 반환합니다.
    global graph
    distances = [INF] * len(graph)
    distances[1] = 0
    for i in range(2, len(graph)):
        que = deque()
        que.append((1, 0))
        visited = [False for _ in range(len(graph))]
        visited[1] = True
        
        while que:
            cur, dist = que.popleft()
            
            if cur == i:
                distances[i] = dist
                
            for neighbor in graph[cur]:
                if visited[neighbor]: continue
                
                que.append((neighbor, dist + 1))
                visited[neighbor] = True
    
    return count_max_value(distances[1:])
    
def solution(n, vertex):
    global graph
    for i in range(n + 1):
        graph.append(set())
    for n1, n2 in vertex:
        graph[n1].add(n2)
        graph[n2].add(n1)
    
    a1 = dijkstra()
    # a2 = bellman_ford()
    # a3 = bfs()
    
    # return a1 if (a1 == a2 and a2 == a3) else -1 
    return a1