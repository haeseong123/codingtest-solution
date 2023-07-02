function solution(tickets) {
    function bfs() {
        function checkRoute(start, temp) {
            if (temp.length === tickets.length) {
                result = [...temp]
                return
            }

            if (!graph.get(start)) return
            
            const neighbors = graph.get(start)
            for (let i = 0; i < neighbors.length; i++) {
                const id = start + i
                if (!visited.has(id)) {
                    temp.push(neighbors[i])
                    visited.add(id)
                    
                    checkRoute(neighbors[i], temp)
                    
                    if (result.length) break
                    
                    visited.delete(id)
                    temp.pop()
                }
            }
        }

        const visited = new Set()
        let result = []
        checkRoute("ICN", [])
        return ["ICN"].concat(result)
    }

    const graph = new Map()
    for (const [from, to] of tickets.sort((a, b) => a[1].localeCompare(b[1]))) {
        const value = graph.get(from) || []
        value.push(to)
        graph.set(from, value)
    }

    return bfs();
}
