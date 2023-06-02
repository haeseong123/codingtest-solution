# 곡괭이: 다이아, 철, 돌
#   0~5개 소유
# 곡괭이로 광물을 캘 때는 피로도가 소모됩니다.

# 다음과 같은 규칙을 지키면서 최소한의 피로도로 광물을 캐려고 합니다.
# - 사용할 수 있는 공괭이중 아무거나 하나를 선택해 광물을 캡니다.
# - 한 번 사용하기 시작한 곡괭이는 사용할 수 없을 때까지 사용합니다.
# - 광물은 주어진 순서대로만 캘 수 있습니다.
# - 광산에 있는 모든 광물을 캐거나, 더 사용할 곡괭이가 없을 때까지 광물을 캡니다.

# 즉, 곡괭이를 하나 선택해서 광물 5개를 연속으로 캐고, 다음 곡괭이를 선택해서 광물 5개를 연속으로 캐는 과정을 반복하며, 더 사용할 곡괭이가 없거나 광산에 있는 모든 광물을 캘 때까지 과정을 반복하면 됩니다.

# picks: 갖고 있는 곡괭이의 개수
# minerals: 광물들의 순서를 나타내는 문자열 배열
# 위 매개변수가 주어질 때, 작업을 끝내기까지 필요한 최소한의 피로도를 반환해주세요.

# <제한사항>
# picks는 [dia, iron, stone]과 같은 구조로 이루어져 있습니다.
# 0 ≤ dia, iron, stone ≤ 5
# dia는 다이아몬드 곡괭이의 수를 의미합니다.
# iron은 철 곡괭이의 수를 의미합니다.
# stone은 돌 곡괭이의 수를 의미합니다.
# 곡괭이는 최소 1개 이상 가지고 있습니다.
# 5 ≤ minerals의 길이 ≤ 50
# minerals는 다음 3개의 문자열로 이루어져 있으며 각각의 의미는 다음과 같습니다.
# diamond : 다이아몬드
# iron : 철
# stone : 돌

# 다섯 개씩 minerals을 나눈 뒤, 
# 각 광물 중 가장 많이 포함하고 있는 광물로 만들어진 곡괭이를 사용하면 가장 효율적이다.
# 5개씩 나눈 minerals를 현재 갖고있는 곡괭이 종류 중 가장 적은 피로도를 사용하는 곡괙이로 캔다.
# 다이아 -> iron -> stone 을 포함하는 개수 순으로 정렬한다. 단, 곡괭이로 캘 수 있을 만큼만 집계한다.
# 정렬한 배열을 순회하며 아래를 수행한다.
# 해당 광물을 현재 갖고있는 곡괭이 중 가장 좋은 곡괭이로 캤을 때 소요되는 피로도를 구하고 합산한다.
# 합산 값을 반환한다.
from collections import Counter

def solution(picks, minerals):
    answer, group = 0, []
    can_mine = min(len(minerals), sum(picks) * 5)
    for i in range(0, can_mine, 5):
        counter = Counter(minerals[i: i+5])
        group.append(( counter["diamond"], counter["iron"], counter["stone"] ))
    group.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    
    for g in group:
        if picks[0]:
            answer += sum(g)
            picks[0] -= 1
        elif picks[1]:
            answer += (g[0] * 5) + g[1] + g[2]
            picks[1] -= 1
        else:
            answer += (g[0] * 25) + (g[1] * 5) + g[2]
            picks[2] -= 1
                
    return answer