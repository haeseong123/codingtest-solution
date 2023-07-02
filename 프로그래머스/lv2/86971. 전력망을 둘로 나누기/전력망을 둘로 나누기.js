function solution(n, wires) {
    function dfs(start) {
        const stack = [start]
        const visited = new Array(n + 1).fill(false);
        visited[start] = true;
        let count = 1;

        while (stack.length) {
            curr = stack.pop()

            for (const neighbor of graph[curr]) {
                if (visited[neighbor]) continue
                stack.push(neighbor)
                visited[neighbor] = true
                count += 1
            }
        }

        return count;
    }

    let answer = Infinity;
    const graph = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of wires) {
        graph[a].push(b);
        graph[b].push(a);
    }
    for (const [a, b] of wires) {
        graph[a] = graph[a].filter((neighbor) => neighbor !== b) 
        graph[b] = graph[b].filter((neighbor) => neighbor !== a) 
        answer = Math.min(answer, Math.abs(n - (dfs(a) * 2)))
        graph[a].push(b)
        graph[b].push(a)
    }
    return answer;
}