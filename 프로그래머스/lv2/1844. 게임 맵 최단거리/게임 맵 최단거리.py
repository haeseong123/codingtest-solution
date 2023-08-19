from collections import deque


def solution(maps):
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    que = deque()
    que.append((0, 0, 1))
    visited = set()
    visited.add((0, 0))

    while que:
        r, c, count = que.popleft()

        if r == len(maps) - 1 and c == len(maps[0]) - 1:
            return count

        for dr, dc in moves:
            nr, nc = dr + r, dc + c

            if (0 <= nr < len(maps)) and (0 <= nc < len(maps[0])) and maps[nr][nc] == 1 and (nr, nc) not in visited:
                que.append((nr, nc, count + 1))
                visited.add((nr, nc))
    
    return -1
