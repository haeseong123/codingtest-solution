# <문제>
# n x m 크기의 격자가 주어집니다.
# (x, y) 에서 출발하여
# (r, c) 에 도착하는
# 총 이동 수가 k 인 경로 중
# 여러 사전 순으로 가장 빠른 경로를 반환해주세요.

# k 만큼 이동하여 도착할 수 없는 경우 "impossible"을 반환합니다.
# 같은 좌표를 두 번 이상 지나갈 수 있습니다.

# <제한사항>
# 2 <= n(미로의 세로 길이), m(미로의 가로 길이)
# 1 <= x, r <= n
# 1 <= y, c <= m
# (x, y) != (r, c)
# 1 <= k <= 2,500

# <풀이>
# impossible이 되는 조건은 아래와 같습니다.
#       - (x, y)에서 (r, c)까지의 최단거리가 k보다 크면 impossible입니다.
#       - (x, y)에서 (r, c)까지의 최단거리가 짝수이면 k도 짝수여야하고,
#           홀수이면 k도 홀수여야 합니다. 이것이 지켜지지 않으면 아니면 impossible입니다.
#           따라서 ((최단거리 - k) % 2) == 0 이어야 합니다.
# 위 impossible에 해당되지 않으면서 도착지에 도착하는 가장 빠른 값을 반환하면 됩니다.
# (l, r, u, d)를 사전 순으로 정렬하면 (d, l, r, u) 입니다. 따라서, 이 순서대로 dfs를 진행해야 합니다.

# 0. ((현재 위치부터 목표 위치까지의 최단거리 - k) % 2) == 0 인지 확인합니다. 아니라면 impossible을 반환합니다.
# 1. dfs를 사용합니다.
#       1-1 (현재 이동한 칸 + 남은 칸 < k)인지 확인합니다. 아니라면 continue합니다.
#       1-2 현재 칸이 목표 칸인지 확인합니다.
#           1-2-1 (이동 칸 == k)인지 확인합니다. 맞다면 str을 반환합니다.
#       1-3 (d, l, r, u)를 순회하며 이동 후의 위치가 유효한 값인지 확인합니다.
#           1-3-1 유효하다면 stack에 넣습니다.
#       1-4 위 1-1~1-3을 stack에 값이 존재할 때까지 반복합니다. 만약 끝까지 반복했음에도 값이 나오지 않는다면 impossible을 반환합니다.
def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solution(n, m, x, y, r, c, k):
    impossible = "impossible"
    
    if (distance(x, y, r, c) - k) % 2 != 0:
        return impossible
    
    def dfs(start_x, start_y):
        stack = [(start_x, start_y, 0, "")]
        # ["d", "l", "r", "u"]인데 stack으로 dfs를 사용하여 찾으니까 역순으로 저장해 놓습니다.
        moves = ["u", "r", "l", "d"]
        # moves의 순서에 맞게 dx, dy를 선언해 놓습니다.
        dxy = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        
        while stack:
            curr_x, curr_y, cnt, ans = stack.pop()
            if cnt + distance(curr_x, curr_y, r, c) > k:
                continue
            if curr_x == r and curr_y == c and cnt == k:
                return ans
            
            for s, (dx, dy) in zip(moves, dxy):
                nx = curr_x + dx
                ny = curr_y + dy
                if 0 < nx <= n and 0 < ny <= m:
                    stack.append((nx, ny, cnt + 1, ans + s))
        return impossible

    return dfs(x, y)