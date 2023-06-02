# bfs로 찾는다.
# 각 위치에서 (상,하,좌,우) visited를 체크한다.
# 도중 G의 위치에 도착하면 cnt를 반환한다.
# 모두 확인했음에도 반환되지 않았다면 -1을 반환한다.

# 현재 위치와 visited를 매개변수로 받는 재귀 함수를 선언한다.
# 해당 위치와 cnt(1)를 que에 넣고 visited를 true로 바꾼다.
# while que:
#   popleft()한다.
#   상-하-좌-우 방면을 순회한다.
#       D를 만나거나 board끝에 다다르는 좌표를 확인한다.
#       해당 좌표를 아직 visited하지 않았다면 que에 넣는다. 이때 cnt + 1 도 함께 넣는다.
#       만약 G를 만난다면 cnt를 반환한다.
# return -1
from collections import deque


def solution(board):
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 상-하-좌-우
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    que = deque()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                que.append((i, j, 0))
                visited[i][j] = True
                break

    while que:
        row, col, cnt = que.popleft()
        if board[row][col] == 'G':
            return cnt

        for move in moves:
            next_r, next_c = row, col
            while (0 <= next_r < len(board)) and (0 <= next_c < len(board[0])) and board[next_r][next_c] != 'D':
                next_r += move[0]
                next_c += move[1]
            next_r -= move[0]
            next_c -= move[1]

            if not visited[next_r][next_c]:
                que.append((next_r, next_c, cnt + 1))
                visited[next_r][next_c] = True

    return -1
