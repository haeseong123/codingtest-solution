# 코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.

# 예를 들어 코니가 가진 옷이 아래와 같고, 오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.

# 코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다. 예를 들어 위 예시의 경우 동그란 안경과 검정 선글라스를 동시에 착용할 수는 없습니다.
# 착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
# 코니는 하루에 최소 한 개의 의상은 입습니다.

# 코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

# map을 사용하여 각 옷을 분류하고
# map을 순회하며 answer = answer * value + 1 을 반복한다.
# 마지막에 -1을 한다.
# 이는 경우의 수를 구하는 것이며, 
# value에 +1을 하는 이유는 해당 부위의 옷을 입지 않을 경우도 고려해야 하기 때문이며, 최종 answer에 -1을 하는 이유는 전체 옷을 아무것도 입지않는 경우를 제외하기 위함입니다.
from functools import reduce

def solution(clothes):
    clothe_map = {}
    for c, _type in clothes:
        clothe_map[_type] = clothe_map.get(_type, 0) + 1
    return (reduce(lambda acc, curr: acc*(curr+1), clothe_map.values(), 1)) - 1
