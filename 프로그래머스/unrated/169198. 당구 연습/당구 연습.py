def get_diff(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)

def solution(m, n, start_x, start_y, balls):
    answer = []
    
    for target_x, target_y in balls:
        distances = []
        # 위
        if start_x != target_x or start_y > target_y:
            distances.append(get_diff(start_x, start_y, target_x, n + (n - target_y)))
        # 아래
        if start_x != target_x or start_y < target_y:
            distances.append(get_diff(start_x, start_y, target_x, target_y * -1))
        # 좌
        if start_y != target_y or start_x < target_x:
            distances.append(get_diff(start_x, start_y, target_x * -1, target_y))
        # 우
        if start_y != target_y or start_x > target_x:
            distances.append(get_diff(start_x, start_y, m + (m - target_x), target_y))
        answer.append(min(distances))
            
    return answer