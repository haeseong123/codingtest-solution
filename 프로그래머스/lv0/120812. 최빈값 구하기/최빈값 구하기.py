from collections import defaultdict


def get_mode_hash(array):
    hash_table = defaultdict(int)  # value의 기본값이 0인 hash_table을 생성합니다.
    max_count = 0  # 빈도수를 나타냅니다.
    mode = -1  # 최빈값을 저장합니다.

    # 1. 입력 배열(array)를 순회하며 각 원소의 빈도를 해시 테이블(또는 딕셔너리)에 저장합니다.
    for key in array:
        hash_table[key] += 1

    # 2. 해시 테이블에서 가장 빈도가 높은 원소를 찾습니다.
    for key, value in hash_table.items():

        # 현재 최빈값의 빈도수보다 더 큰 빈도수를 갖는 원소를 찾으면..
        if max_count < value:

            # 최빈값과 빈도수를 갱신합니다.
            mode, max_count = key, value

        # 현재 최빈값의 빈도수와 같은 빈도수를 갖는 원소를 찾으면..
        elif max_count == value:

            # 최빈값을 -1로 바꿉니다. (문제 설명에 -1로 하라고 나와있습니다.)
            mode = -1

    # 3. 최빈값을 반환합니다.
    return mode

def solution(array):
    return get_mode_hash(array)