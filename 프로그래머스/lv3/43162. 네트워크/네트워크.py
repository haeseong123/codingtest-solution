# <문제 설명>
# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 
# 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 
# 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 
# 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

# 컴퓨터의 개수 n, 
# 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
# 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

# <제한사항>
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.

# <문제 풀이>
# union find하면 될듯한데...
# 혹은 그래프를 만들고 bfs/dfs로 순회하며 갯수를 cnt해도 될 듯.

# union find 풀이
# n에 따른 union_find 배열을 생성한다.
# computers를 순회하며 아래를 수행한다. == for i in range(n):
#   [x1, x2, ..., xn]을 순회하며 아래를 수행한다. == for j, neighbor in enumberate(computer):
#       if j == i: continue
#       union(i, j)
# union_find를 순회하며 아래를 수행한다.
#   if find(i) not in cnt_set:
#       cnt_set.add(find(i))
# return len(cnt_set)

# dfs/bfs 풀이
# computers를 순회하며 아래를 수행한다. == for i, computer in enumerate(computers):
#   if visited[i]: continue
#   for neighbor in computer:
#       if visited[neighbor] or i == neighbor: continue
#       dfs(neighbor)
#       cnt += 1
# return cnt
uf = []

def union(x1, x2):
    global uf
    r1 = find(x1)
    r2 = find(x2)
    
    if r1 == r2:
        return
    
    uf[r2] = r1

def find(x):
    global uf
    
    if uf[x] == x:
        return x
    
    uf[x] = find(uf[x])
    return uf[x]


def dfs(graph, visited, start):
    stack = [(graph[start], start)]
    visited[start] = True

    while stack:
        neighbors, idx = stack.pop()

        for neighbor, is_connected in enumerate(neighbors):
            if visited[neighbor] or not is_connected: continue
            stack.append((graph[neighbor], neighbor))
            visited[neighbor] = True
    
def solution(n, computers):
    global uf
    for i in range(n):
        uf.append(i)
        
    for i in range(len(computers)):
        for j, is_connected in enumerate(computers[i]):
            if i == j: continue
            if is_connected:
                union(i, j)
    
    root_set = set()
    for x in uf:
        root = find(x)
        if root in root_set: continue
        root_set.add(root)
    union_find_answer = len(root_set)
    
    dfs_answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i]: continue
        dfs(computers, visited, i)
        dfs_answer += 1
    
    return union_find_answer if union_find_answer == dfs_answer else -1
