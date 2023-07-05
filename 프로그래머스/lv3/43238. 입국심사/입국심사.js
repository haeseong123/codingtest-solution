// <문제 설명>
// 심사관마다 심사 시간이 다릅니다.
// 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.

// 아래 매개변수가 주어질 때 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 반환해 주세요.
// n: 입국심사를 기다리는 사람 수
// times: 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열

// <제한사항>
// 입국심사를 기다리는 사람은 1 <= n <= 1,000,000,000
// 1 <= times[i] <= 1,000,000,000 (분 단위)
// 1 <= times.length <= 100,000
function solution(n, times) {
    let answer = 0;
    times.sort((a, b) => {
        if (a < b) return -1
        if (a === b) return 0
        if (a > b) return 1
    });
    let l = 0,
        r = n * times[times.length - 1];
    
    while (l <= r) {
        const m = Math.floor((l + r) / 2)
        let sum = 0
        for (const time of times) {
            sum += Math.floor(m / time)
        }
        if (sum < n) {
            l = m + 1
        } else {
            r = m - 1
            answer = m
        }
    }
    
    return answer
}