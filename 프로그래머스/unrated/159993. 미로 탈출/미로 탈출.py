# 길찾기 문제인데, 레버를 먼저 방문한 뒤 exit해야 한다.
# bfs로 "L"까지 가고 해당 위치서부터 "X"까지 가는 거리를 합하면 된다.
# 단, 길이 막혀 갈 수 없는 경우도 있다. 이 경우 -1을 반환한다.
# 길찾기 문제인데, 레버를 먼저 방문한 뒤 exit해야 한다.
# bfs로 "L"까지 가고 해당 위치서부터 "X"까지 가는 거리를 합하면 된다.
# 단, 길이 막혀 갈 수 없는 경우도 있다. 이 경우 -1을 반환한다.
from collections import deque


def solution(maps):
    def bfs(sr, sc, target):
        moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
        que = deque()
        que.append((sr, sc, 0))
        visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
        visited[sr][sc] = True

        while que:
            r, c, acc = que.popleft()

            if maps[r][c] == target:
                return r, c, acc

            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and maps[nr][nc] != "X" and not visited[nr][nc]:
                    que.append((nr, nc, acc + 1))
                    visited[nr][nc] = True

        return -1, -1, -1
    
    start_r, start_c = 0, 0
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == "S":
                start_r, start_c = r, c
                break
    
    answer = 0
    for target in ("L", "E"):
        start_r, start_c, acc = bfs(start_r, start_c, target)
        if acc == -1:
            answer = -1
            break
        else:
            answer += acc
            
    return answer