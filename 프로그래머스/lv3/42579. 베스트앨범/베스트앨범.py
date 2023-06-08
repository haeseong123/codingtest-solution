# <문제 설명>
# 베스트 앨범을 출시하려 합니다.
# 노래를 수록하는 기준은 아래와 같습니다.
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

# 아래 매개변수가 주어질 때 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 반환해 주세요.
# genres: 노래의 장르를 나타내는 문자열 배열
# plays: 노래별 재생 횟수를 나타내는 정수 배열

# <제한사항>
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.

# <풀이>
# genres를 순회하며 {type:[총 재생 수, [(재생 수, idx), (재생 수, idx), ...]]} 형태의 dict를 생성합니다.
# dict를 list형태로 변환합니다.
# list를 아래 기준에 따라 정렬합니다.
#   1. 총 재생 수 내림차순
# list의 요소에 있는 [(재생 수, idx), (), ...]를 아래 기준에 따라 정렬합니다.
#   1. 장르 내에서 많이 재생된 노래 내림차순
#   2. 장르 내에서 idx 오름차순
# list를 순회하며 장르 내의 idx를 answer에 append합니다.
# answer를 반환합니다.

def solution(genres, plays):
    dictionary = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        value = dictionary.get(g, [0, []])
        value[0] += p
        value[1].append((p, i))
        dictionary[g] = value
    
    answer = []
    sorted_list = sorted(list(dictionary.values()), key=lambda x: -x[0])
    for _, play_idx_arr in sorted_list:
        for p, i in sorted(play_idx_arr, key=lambda x: (-x[0], x[1]))[:2]:
            answer.append(i)
    return answer