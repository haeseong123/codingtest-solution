import heapq

graph = []
INF = float('inf')

def count_max_value(arr):
    _max = max(arr)
    count = 0
    for n in arr:
        if n == _max: count += 1
    return count

def dijikstra():
    distances = [INF] * len(graph)
    distances[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))

    for _ in range(len(graph) - 2):
        dist, u = heapq.heappop(heap)

        for v in graph[u]:
            n_dist = dist + 1
            if distances[v] > n_dist:
                distances[v] = n_dist
                heapq.heappush(heap, (n_dist, v))
    return count_max_value(distances[1:])

def bellman_ford():
    distances = [INF] * len(graph)
    distances[1] = 0
    
    for _ in range(len(graph) - 2):
        for u in range(1, len(graph)):
            for v in graph[u]:
                if distances[v] > distances[u] + 1:
                    distances[v] = distances[u] + 1
    return count_max_value(distances[1:])
    
def solution(n, vertex):
    for i in range(n + 1):
        graph.append(set())
    for a, b in vertex:
        graph[a].add(b)
        graph[b].add(a)
        
    d = dijikstra()
    # b = bellman_ford()
        
    # return d if d == b else - 1
    return d
