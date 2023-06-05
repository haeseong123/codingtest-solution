# 1. 'X'가 'O'보다 많을 수 없습니다.
# 2. 'O'가 'X'보다 2개 이상 많을 수 없습니다.
# 3. 'O'가 승리할 때 'X'가 승리할 수 없으며, 'X'의 개수는 'O'보다 1만큼 더 작아야합니다.
# 4. 'X'가 승리할 때 'O'와 개수가 같아야 합니다.

def check_winner(board, player):
    # 가로, 세로, 대각선 중 3개가 같은 표시가 있는지 확인
    for i in range(3):
        # 가로
        if all(board[i][j] == player for j in range(3)):
            return True
        # 세로
        if all(board[j][i] == player for j in range(3)):
            return True
    # 촤측 상단에서 우측 하단으로의 대각선
    if all(board[i][i] == player for i in range(3)):
        return True
    # 우측 상단에서 좌측 하단으로의 대각선
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def solution(board):
    # 'O'와 'X'의 개수 카운트
    count_O = sum(row.count('O') for row in board)
    count_X = sum(row.count('X') for row in board)
    
    if count_O < count_X or count_O > count_X + 1:
        return 0
    
    if check_winner(board, 'O'):
        if check_winner(board, 'X'):
            return 0
        if count_O != count_X + 1:
            return 0
    elif check_winner(board, 'X'):
        if count_O != count_X:
            return 0
    
    return 1