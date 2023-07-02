function solution(routes) {
    let answer = 0;
    routes.sort((a, b) => a[1] - b[1])
    while (routes.length) {
        value = routes[0][1]
        routes = routes.filter(r => r[0] > value)
        answer += 1
    }
    return answer;
}