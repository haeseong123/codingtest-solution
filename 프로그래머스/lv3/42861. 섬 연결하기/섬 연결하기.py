# <문제 설명>
# n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 
# 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

# 다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 
# 예를 들어 A 섬과 B 섬 사이에 다리가 있고, 
# B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

# <제한사항>
# 섬의 개수 n은 1 이상 100 이하입니다.
# costs의 길이는 ((n-1) * n) / 2이하입니다.
# 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, 
#   costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
# 같은 연결은 두 번 주어지지 않습니다. 
#   또한 순서가 바뀌더라도 같은 연결로 봅니다. 
#   즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
# 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 
#   이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
# 연결할 수 없는 섬은 주어지지 않습니다.

# <풀이>
# union-find을 사용하면 될 것 같습니다.
# union-find 배열을 생성합니다.
# costs를 오름차순으로 정렬합니다.
# costs를 순회하며 아래를 수행합니다.
#   해당 노드들의 root 노드가 같은지 확인합니다. 같다면 continue 합니다.
#   다르다면 union 작업을 수행하고 answer += coast를 합니다.
# answer를 반환합니다.

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

def solution(n, costs):
    global uf
    uf = [i for i in range(n)]
    answer = 0
    
    for x1, x2, cost in sorted(costs, key=lambda x: x[2]):
        r1 = find(x1)
        r2 = find(x2)
        if r1 == r2: continue
        
        answer += cost
        union(r1, r2)
    
    return answer