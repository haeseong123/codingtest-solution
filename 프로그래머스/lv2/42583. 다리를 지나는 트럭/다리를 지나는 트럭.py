def solution(bridge_length, weight, truck_weights):
    # 다리에 있는 트럭 옮기고
    # 대기 큐에있는 트럭 중 가장 앞에 있는 트럭을 다리에 올릴 수 있으면 올리고
    # 이거를 대기 큐가 텅 비고, 다리에 있는 트럭이 없을 때까지 반복
    bridge, time = [], 0
    while truck_weights or bridge:
        time += 1
        if bridge:
            if bridge[0][0] == bridge_length:
                weight += bridge.pop(0)[1]
            for i in range(len(bridge)):
                bridge[i][0] += 1 
        
        if truck_weights and truck_weights[0] <= weight:
            tw = truck_weights.pop(0)
            bridge.append([1, tw])
            weight -= tw
        
    return time