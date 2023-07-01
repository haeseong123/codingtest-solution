// 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 
// 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
// 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 
// 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 
// 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

// 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 
// 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.


// 시간을 +1 합니다.
// 다리 위에 있는 트럭들을 한 칸 전진 시킵니다.
// 다리 바깥에서 기다리는 트럭들 중 제일 앞 트럭을
//      다리 위에 올릴 수 있다면 올립니다.
// 이를 다리 바깥에서 기다리는 트럭이 텅 빌 때 까지 반복합니다.
// 다리 위에 있는 트럭을 모두 보냅니다.
//      이때 계산은 
//      시간 += 제일 뒤에 있는 트럭의 남은 시간
// 시간을 반환합니다.
function solution(bridge_length, weight, truck_weights) {
    let answer = 0;
    const bridge = [];
    // 모든 트럭 다리에 올리기
    while (truck_weights.length) {
        answer += 1;
        // 다리에 올려져 있는 트럭 앞으로 한 칸씩 옮기기
        if (bridge.length) {
            for (let i = 0; i < bridge.length; i++) {
                bridge[i][0] += 1;
            }
            if (bridge[0][0] === bridge_length) {
                weight += bridge.shift()[1];
            }            
        }
        // 기다리는 트럭을 다리에 올릴 수 있다면 올리기
        if (weight >= truck_weights[0]) {
            const truck = truck_weights.shift() 
            weight -= truck;
            bridge.push([0, truck]);
        }
    }
    
    // 다리에 올린 트럭 내리기
    if (bridge.length) {
        answer += bridge_length - bridge[bridge.length - 1][0];
    }
    
    return answer;
}