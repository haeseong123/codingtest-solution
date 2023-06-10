# <문제 설명>
# ROR 게임은 두 팀으로 나누어서 진행하며, 
# 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. 
# 따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.

# 지금부터 당신은 한 팀의 팀원이 되어 게임을 진행하려고 합니다. 
# 다음은 5 x 5 크기의 맵에, 당신의 캐릭터가 (행: 1, 열: 1) 위치에 있고, 
# 상대 팀 진영은 (행: 5, 열: 5) 위치에 있는 경우의 예시입니다.

# 위 그림에서 검은색 부분은 벽으로 막혀있어 갈 수 없는 길이며, 
# 흰색 부분은 갈 수 있는 길입니다. 
# 캐릭터가 움직일 때는 동, 서, 남, 북 방향으로 한 칸씩 이동하며, 
# 게임 맵을 벗어난 길은 갈 수 없습니다.
# 아래 예시는 캐릭터가 상대 팀 진영으로 가는 두 가지 방법을 나타내고 있습니다.

# 게임 맵의 상태 maps가 매개변수로 주어질 때, 
# 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. 
# 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

# <제한사항>
# maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
# n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
# maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
# 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

# <문제 풀이>
# 캐릭터는 상-하-좌-우로 움직일 수 있고 목표 지점까지의 최단거리를 구하는 문제입니다.
# 단, 목표 지점까지 도착하지 못하는 경우도 있습니다.

# maps의 (0, 0) 위치에서 캐릭터가 출발합니다.
# 움직일 수 있는 방향은 오직 상-하-좌-우 이므로 순서에 맞춰 [(-1, 0), (1, 0), (0, -1), (0, 1)] 입니다.
# 또한, 최단 거리를 구하는 문제이므로 한 번 지난 길을 다시 갈 필요는 없습니다.
# 따라서 visited 배열을 선언하여 한 번 방문한 위치는 중복하여 방문하지 않도록 합니다.
# bfs와 visited 배열을 사용하여 문제를 풀면 됩니다.
from collections import deque

def solution(maps):
    def bfs():
        moves = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 상 하 좌 우
        que = deque()
        que.append((0, 0, 1))
        visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
        visited[0][0] = True
        
        while que:
            row, col, cnt = que.popleft()
            
            if row == len(maps) - 1 and col == len(maps[0]) - 1:
                return cnt
            
            for move in moves:
                n_row, n_col = row + move[0], col + move[1]
                if not (0 <= n_row < len(maps)) or not (0 <= n_col < len(maps[0])) or not maps[n_row][n_col] or visited[n_row][n_col]:
                    continue
                que.append((n_row, n_col, cnt + 1))
                visited[n_row][n_col] = True
        
        return -1
    
    return bfs()