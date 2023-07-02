// 단어를 노드로 하여서
// 차이가 1개 나는 단어들을 간선으로 잇고
// begin부터 target까지 최단거리 bfs
function solution(begin, target, words) {
    function isNeighbor(a, b) {
        let diffCount = 0
        for (let i = 0; i < a.length; i++) {
            if (a[i] !== b[i]) {
                diffCount += 1
                if (diffCount > 1) {
                    return false
                }
            }
        }
        return diffCount === 1 ? true : false
    }
    
    function bfs() {
        const que = [[begin, 0]]
        const visited = new Set()
        visited.add(begin)
        
        while(que.length) {
            const [curr, count] = que.shift()
            
            if (curr === target) {
                return count
            }
            
            for (const neighbor of graph.get(curr).values()) {
                if (visited.has(neighbor)) continue
                que.push([neighbor, count + 1])
                visited.add(neighbor)
            }
        }
        
        return 0
    }
    
    words.push(begin)
    const graph = new Map()
    for (const word of words) {
        const value = new Set()        
        for (const w of words) {
            if (w !== word && isNeighbor(w, word)) {
                value.add(w)
            }
        }
        graph.set(word, value)
    }
    
    return bfs();
}