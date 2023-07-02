// computers에 담긴 연결 따라 연결 시켜주고
// dfs 돌리면서 같은 네트워크 체크 cnt += 1
// return cnt
function solution(n, computers) {
    function dfs(start) {
        const stack = [start]
        visited.add(start)
        
        while (stack.length) {
            const curr = stack.pop()
            
            for (let i = 0; i < n; i++) {
                if (visited.has(i) || graph[curr][i] === 0 || curr === i) continue
                stack.push(i)
                visited.add(i)
            }
        }
    }
    
    const graph = Array(n).fill().map((_, i) => computers[i])
    const visited = new Set()
    // const visited = Array(n).fill().map(() => new Set())
    // visited.forEach((s, i) => s.add(i))
    
    let answer = 0
    for (let i = 0; i < n; i++) {
        if (visited.has(i)) continue
        dfs(i)
        answer += 1
    }
    return answer
}