# 0으로 n * n 배열을 초기화 합니다.
# direction을 바꿔가며 값을 넣습니다.
#   0이 아닌 값을 만날 때 direction을 바꿉니다.
def solution(n):
    curr_r, curr_c, cnt = 0, 0, 0
    answer = [[0 for _ in range(n)] for _ in range(n)]
    answer[0][0] = 1
    direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
    i = 0
    while True:
        (dr, dc) = direction[i]
        nxt_r = curr_r + dr
        nxt_c = curr_c + dc
        i = (i + 1) % 4

        if nxt_r < 0 or n <= nxt_r or nxt_c < 0 or n <= nxt_c or answer[nxt_r][nxt_c] != 0:
            break

        while 0 <= nxt_r < n and 0 <= nxt_c < n and answer[nxt_r][nxt_c] == 0:
            answer[nxt_r][nxt_c] = answer[curr_r][curr_c] + 1
            curr_r, curr_c = nxt_r, nxt_c
            nxt_r += dr
            nxt_c += dc

    return answer
