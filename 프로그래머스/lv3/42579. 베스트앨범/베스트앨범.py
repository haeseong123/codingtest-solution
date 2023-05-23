# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아
# 베스트 앨범을 출시하려 합니다.
# 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
#   1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
#   2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
#   3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

# 노래의 장르를 나타내는 문자열 배열 genres와
# 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하세요.

# 풀이
# 1. genres를 순회하며 {장르:[총 재생횟수, [(고유 번호, 재생 횟수), (고유 번호, 재생 횟수), ...]]} map을 생성한다. O(N)
# 2. map을 통해 array를 생성한다. [[총 재생 횟수, [(고유 번호, 재생 횟수), ...]]]배열로 바꾼다. O(N)
# 3. array를 총 재생 횟수 내림차순으로 정렬한다. O(n logn)
# 4. 앞에서부터 순회하며 아래를 실행한다. O(N)
# 5. [(고유 번호, 재생 횟수), ...] 배열을 재생 횟수 내림차순, 고유 번호 오름차순으로 정렬한다.
# 6. [(고유 번호, 재생 횟수), ...] 배열을 최대 두 번 순회하며 아래를 실행한다.
# 7. answer에 고유 번호를 추가한다.
# 8. answer를 반환한다.
def solution(genres, plays):
    answer = []
    genres_map = {}
    # 1
    for i, (g, p) in enumerate(zip(genres, plays)):
        values = genres_map.get(g, [0, []])
        values[0] += p
        values[1].append((i, p))
        genres_map[g] = values
    # 2, 3
    genres_arr = sorted([g for g in genres_map.values()], key=lambda x: x[0], reverse=True)
    # 4
    for g in genres_arr:
        # 5
        g[1].sort(key=lambda x: (-x[1], x[0]))
        # 6
        for i in range(min(2, len(g[1]))):
            # 7
            answer.append(g[1][i][0])
    # 8
    return answer