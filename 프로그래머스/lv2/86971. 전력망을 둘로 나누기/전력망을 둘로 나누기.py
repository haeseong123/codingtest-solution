from collections import deque

def solution(n, wires):
    min_diff = n - 2
    graph = [[] for _ in range(n+1)]
    # 연결
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        que = deque([start])
        visited = [False] * (n+1)
        visited[start] = True
        cnt = 1
        
        while que:
            v = que.popleft()
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    que.append(neighbor)
                    visited[neighbor] = True
                    cnt += 1
        return cnt
    
    # 연결을 하나씩 끊어가면서 확인하기
    for a,b in wires:
        # 끊기
        graph[a].remove(b)
        graph[b].remove(a)
        
        # 차이를 계산하고 min_diff 갱신
        min_diff = min(abs(bfs(a) - bfs(b)), min_diff)
        
        # 다시 연결
        graph[a].append(b)
        graph[b].append(a)
    
    return min_diff