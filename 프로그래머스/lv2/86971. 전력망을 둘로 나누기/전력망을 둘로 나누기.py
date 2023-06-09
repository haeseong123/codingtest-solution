# <문제 설명>
# n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 
# 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 
# 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

# 송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 
# 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 
# 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

# <제한사항>
# n은 2 이상 100 이하인 자연수입니다.
# wires는 길이가 n-1인 정수형 2차원 배열입니다.
#   wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
#   1 ≤ v1 < v2 ≤ n 입니다.
#   전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

# <문제 풀이>
# "유니온 파인드"혹은 "dfs/bfs"를 사용하여 풀 수 있을 것 같다.

# union-find
# 각 노드를 union-find 베열에 초기화 한다. [1, 2, 3, 4, ..., n]
# wires를 순회하며 union 작업을 수행한다.
# wires를 순회하며 아래 작업을 수행한다.
#   해당 wire를 끊는다.
#   union-find 배열을 순회하며 루트 노드가 서로 다른 것의 개수를 카운트한다.
#   answer = min(answer, abs(cnt1 - cnt2))
#   해당 wire를 다시 연결한다.
# return answer

# dfs/bfs
# 각 노드를 배열에 초기화한다. [[], [], [], ..., []]
# wires를 순회하며 연결을 수행한다.
# wires를 순회하며 아래 작업을 수행한다.
#   해당 wire를 끊는다.
#   visited = [False] * N
#   tmp = []
#   for i in range():
#       if not visited[i]:
#            tmp.append(count_with_dfs/bfs(arr[i]))
#   answer = min(answer, abs(tmp[0] - tmp[1]))
#   해당 wire를 다시 연결한다.
# return answer


# <UNION-FIND>
def union(arr, n1, n2):
    # 두 노드를 합칩니다.
    # 합친다는 것은 같은 루트 노드를 가리키게 하는 것입니다.
    r1 = find(arr, n1)
    r2 = find(arr, n2)
    
    if r1 == r2:
        return
    
    arr[r2] = r1

def find(arr, n):
    # 루트 노드를 찾습니다.
    if arr[n] == n:
        return n
    
    arr[n] = find(arr, arr[n])
    return arr[n]

# <DFS/BFS>
def dfs():
    print()
    
def solution(n, wires):
    # 유니온 파인드를 사용한 풀이
    answer1 = float("inf")
    for i in range(n - 1):
        arr = [j for j in range(n + 1)]
        for k, wire in enumerate(wires):
            if i == k:
                continue
            union(arr, wire[0], wire[1])
        cnt = {}
        for node in arr[1:]:
            root = find(arr, node) 
            if root in cnt:
                cnt[root] += 1
            else:
                cnt[root] = 1
        tmp = list(cnt.values())
        answer1 = min(answer1, abs(tmp[0] - tmp[1]))
    return answer1
    # dfs/bfs를 사용한 풀이
#     answer2 = 0
    
    
#     return answer1 if answer1 == answer2 else -1