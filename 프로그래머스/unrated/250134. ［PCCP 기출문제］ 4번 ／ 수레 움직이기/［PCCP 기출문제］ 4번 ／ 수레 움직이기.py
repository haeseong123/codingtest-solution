from collections import deque
import copy


def solution(maze):
    def get_next_positions(curr, v, t):
        if curr == t:
            return [curr]

        (r, c) = curr
        positions = []

        for (dr, dc) in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < len(maze)) and (0 <= nc < len(maze[0])) and ((nr, nc) not in v) and (maze[nr][nc] != 5):
                positions.append((nr, nc))

        return positions

    # 초기화
    directions, que = ((-1, 0), (1, 0), (0, -1), (0, 1)), deque()
    visited, starting_position, target = [set(), set()], [None, None], [None, None]
    for (i, row) in enumerate(maze):
        for (j, info) in enumerate(row):
            if info == 1:
                starting_position[0] = (i, j)
                visited[0].add(starting_position[0])
            elif info == 2:
                starting_position[1] = (i, j)
                visited[1].add(starting_position[1])
            elif info == 3:
                target[0] = (i, j)
            elif info == 4:
                target[1] = (i, j)

    # BFS
    que.append((starting_position[0], starting_position[1], 0, visited))
    while que:
        red, blue, count, visits = que.popleft()

        if red == target[0] and blue == target[1]:
            return count

        next_reds = get_next_positions(red, visits[0], target[0])
        next_blues = get_next_positions(blue, visits[1], target[1])

        for next_red in next_reds:
            for next_blue in next_blues:
                if next_red == next_blue or (next_red == blue and next_blue == red):
                    continue

                copy_visits = copy.deepcopy(visits)
                copy_visits[0].add(next_red)
                copy_visits[1].add(next_blue)

                que.append((next_red, next_blue, count + 1, copy_visits))

    return 0
