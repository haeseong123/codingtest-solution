# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다.
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
# 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며,
# 다리는 weight 이하까지의 무게를 견딜 수 있습니다.
# 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

# 아래 매개변수가 주어질 때, 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 반환해 주세요.
# bridge_length: 다리에 올라갈 수 있는 트럭 수
# weight: 다리가 견딜 수 있는 무게
# truck_weights: 트럭 별 무게

# <제한 조건>
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.
# 트럭은 1초에 1만큼 이동합니다.

# <문제 풀이>
# 1초가 지나면 다리 위에 있는 트럭들이 모두 1만큼 전진합니다.
# 맨 앞의 트럭이 다리를 통과했다면 weight에 통과한 트럭의 무게를 더합니다.
# 대기 트럭의 맨 앞 트럭이 들어갈 수 있는 공간이 생기며, 이때 하중이 허락한다면(weight >= truck_weight) 대기 트럭 하나가 진입할 수 있습니다.
#   만약 대기 트럭이 진입했다면 weight에 진입한 트럭의 무게를 뺍니다.
# 이 과정을 대기 트럭이 모두 다리를 건널 때까지 반복합니다.
from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_size = len(truck_weights)
    time, pass_trucks = 0, []
    ing_trucks = deque()
    truck_weights = deque(truck_weights)
    
    while len(pass_trucks) < truck_size:
        time += 1
        for truck in ing_trucks:
            truck[0] += 1
            
        if ing_trucks and ing_trucks[0][0] == bridge_length:
            _, truck_weight =  ing_trucks.popleft()
            pass_trucks.append(truck_weight)
            weight += truck_weight
        
        if truck_weights and weight >= truck_weights[0]:
            weight -= truck_weights[0]
            ing_trucks.append([0, truck_weights.popleft()])
            
    return time

