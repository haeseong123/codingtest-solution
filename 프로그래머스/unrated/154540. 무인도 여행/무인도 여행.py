# <문제>
# 무인도로 갈 것입니다.
# 격자 칸이 주어지며
# 각 칸에는 'X' 또는 1~9 사이의 자연수가 적혀있습니다.
# 지도의 'X'는 바다를 나타내며
# 숫자는 무인도를 나타냅니다.
# 이때, 상-하-좌-우로 연결되는 땅들은 하나의 무인도를 이룹니다.
# 각 칸에 적힌 숫자는 식량을 나타내는데 이 수는 각 무인도에서 얼마만큼 머물 수 있는지를 나타냅니다.
# 각 섬에서 최대 며칠씩 머물 수 있는지 나타내는 배열을 오름차순으로 담아 반환해주세요.

# <제한사항>
# 3 ≤ maps의 길이 ≤ 100
#   3 ≤ maps[i]의 길이 ≤ 100
#   maps[i]는 'X' 또는 1 과 9 사이의 자연수로 이루어진 문자열입니다.
#   지도는 직사각형 형태입니다.

# <문제풀이>
# dfs/bfs를 통해 주어진 시작점에서 출발하여 모든 도달가능한 경로에 있는 수를 합하고 answer 배열에 넣습니다.
# answer 배열을 정렬한 뒤 반환합니다.
# 만약 answer의 크기가 0이라면 [-1] 을 반환합니다.

def solution(maps):
    def dfs(start_i, start_j):
        moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
        stack = [(start_i, start_j)]
        visited.add((start_i, start_j))
        acc = int(maps[start_i][start_j])
        
        while stack:
            i, j = stack.pop()
            
            for di, dj in moves:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]) and maps[ni][nj] != 'X' and (ni, nj) not in visited:
                    stack.append((ni, nj))
                    visited.add((ni, nj))
                    acc += int(maps[ni][nj])
        return acc
    
    
    visited = set()
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and (i, j) not in visited:
                answer.append(dfs(i, j))
                
    return sorted(answer) if answer else [-1]