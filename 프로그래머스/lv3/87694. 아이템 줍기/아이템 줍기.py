# 전체 map을 모두 0으로 채운다.
# 전달받은 사각형을 순회하며 아래를 수행한다.
#   사각형의 테두리를 전부 1로 채운다.
#   단, 채워야 할 테두리가 -1에 위치하였다면 그대로 둔다
#   사각형의 내부를 전부 -1로 채운다.

# 위 과정을 통하여 graph를 만듭니다.
# graph를 가지고 bfs를 수행하여 목적지까지 가는 최단 경로를 구합니다.
# 이떄, 캐릭터는 상-하-좌-우 네 가지로만 움직일 수 있으며
#   방문한 좌표의 재방문은 허용되지 않습니다.
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    myX, myY, targetX, targetY = characterX << 1, characterY << 1, itemX << 1, itemY << 1
    # map / visited / moves 생성
    matrix = [[0 for _ in range(101)] for _ in range(101)]
    visited = [[False for _ in range(101)] for _ in range(101)]
    moves = ((1, 0), (-1, 0), (0, -1), (0, 1)) # 상 하 좌 우
    
    # graph 생성 (map을 그래프로 쓸 거임)
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 << 1, y1 << 1, x2 << 1, y2 << 1
        # 좌변
        for ny in range(y1, y2 + 1):
            if matrix[x1][ny] == -1: continue
            matrix[x1][ny] = 1
        # 밑변
        for nx in range(x1, x2 + 1):
            if matrix[nx][y1] == -1: continue
            matrix[nx][y1] = 1
        # 윗변
        for nx in range(x1, x2 + 1):
            if matrix[nx][y2] == -1: continue
            matrix[nx][y2] = 1
        # 우변
        for ny in range(y1, y2 + 1):
            if matrix[x2][ny] == -1: continue
            matrix[x2][ny] = 1
        # 속 -1로 채우기
        for nx in range(x1 + 1, x2):
            for ny in range(y1 + 1, y2):
                matrix[nx][ny] = -1
    
    # bfs 수행
    que = deque()
    que.append((myX, myY, 0))
    visited[myX][myY] = True

    while que:
        x, y, dist = que.popleft()

        if x == targetX and y == targetY:
            return dist >> 1

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (0 <= nx < 101) and (0 <= ny < 101) and (matrix[nx][ny] == 1) and (not visited[nx][ny]):
                que.append((nx, ny, dist + 1))
                visited[nx][ny] = True
    
    return -1