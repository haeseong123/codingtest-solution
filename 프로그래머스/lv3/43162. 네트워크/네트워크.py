def dfs(graph, start, visited):
    stack = [start]
    
    while stack:
        for neighbor in graph[stack.pop()]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

def solution(n, computers):
    graph = [set() for _ in range(len(computers))]
    for i, c in enumerate(computers):
        for j, neighbor in enumerate(c):
            if i == j: continue
            if neighbor == 0: continue
            graph[i].add(j)
    
    visited = set()
    count = 0
    for i, node in enumerate(graph):
        if i in visited: continue
        dfs(graph, i, visited)
        count += 1
    return count