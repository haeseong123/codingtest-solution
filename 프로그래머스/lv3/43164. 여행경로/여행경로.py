# <문제 설명>
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 
# 항상 "ICN" 공항에서 출발합니다.

# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 
# 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# <제한사항>
# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

# <문제 풀이>
# "ICN" 에서 출발하고 항상 알파벳 순서가 앞서는 경로를 우선 탐색합니다.
# 탐색 도중 사용하지 않은 티켓이 남았는데 움직일 수 없거나, 다면 해당 경로 탐색을 취소하고, 다음 우선 경로를 탐색합니다.
# 따라서 분기를 만나면 visitied를 deppcopy해서 사용해야 한다는 것입니다.
# 이는 dfs로 구현할 수 있습니다.

# 또한 알파벳 순서대로 티켓을 사용하기 위해 for 문을 사용해야 할 것입니다.
# 이를 구현하면 됩니다.

# 1. visited 배열을 선언합니다. 모두 False로 초기화합니다.
# 2. tickets를 순회하며 아래를 수행합니다.
# 이는 graph를 만드는 작업이며, graph는 {"출발 공항": ["도착 공항", "", ...]}으로 배열은 알파벳 오름차순으로 정렬되어 있어야 합니다.
#   2-1 value = graph.get("출발 위치", [])
#   2-2 value.append("도착 위치")
# 3. graph를 순회하며 배열을 정렬해 줍니다.
# 4. dfs를 수행합니다.
def solution(tickets):
    def is_all_visit():
        for visit in visited.values():
            if not all(visit): return False
        return True
        
    def dfs(stack, res, start):
        nonlocal answer
        
        if is_all_visit():
            answer = res.copy()
            return
        
        if start not in graph: 
            return
        
        for i, dest in enumerate(graph[start]):
            if visited[start][i]: continue
            
            stack.append(dest)
            res.append(dest)
            visited[start][i] = True
            
            dfs(stack, res, dest)
            if answer: return
            
            stack.pop()
            res.pop()
            visited[start][i] = False
            
    visited = {} 
    graph = {}
    answer = []
    
    for origin, dest in tickets:
        dest_arr = graph.get(origin, [])
        dest_arr.append(dest)
        graph[origin] = dest_arr
    for dest_arr in graph.values():
        dest_arr.sort()
    for origin in graph:
        visited[origin] = [False for _ in range(len(graph[origin]))]
        
    dfs([], ["ICN"], "ICN")
    
    return answer