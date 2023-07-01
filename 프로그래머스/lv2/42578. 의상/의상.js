// 옷의 종류에 따라 나눈 뒤
// 해당 옷을 입지 않는 경우까지 모두 계산을 하고
// 최종 값에서 모든 옷을 입지 않는 경우 하나를 제외한 뒤 반환합니다.
function solution(clothes) {
    const map = new Map();
    
    for (const [name, type] of clothes) {
        const names = map.get(type) || [];
        names.push(name);
        map.set(type, names);
    }
    
    let answer = 1
    for (const names of map.values()) {
        answer *= (names.length + 1);
    }
    return answer - 1;
}