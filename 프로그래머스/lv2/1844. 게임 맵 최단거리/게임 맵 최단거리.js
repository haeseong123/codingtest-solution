function solution(maps) {
    function bfs() {
        const que = [[0, 0, 1]]
        visited[0][0] = 1
        
        while (que.length) {
            const [r, c, count] = que.shift()
            
            if (r === n - 1 && c === m - 1) {
                return count
            }
            
            for (const [dr, dc] of moves) {
                const nr = r + dr,
                      nc = c + dc
                if ((0 <= nr && nr < n) && 
                    (0 <= nc && nc < m) && 
                    visited[nr][nc] === 0 && 
                    maps[nr][nc] === 1) 
                {
                    que.push([nr, nc, count + 1])
                    visited[nr][nc] = 1
                }
            }
        }
        
        return -1
    }
    
    const n = maps.length,
          m = maps[0].length
    const moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    const visited = Array(n).fill().map(()=> Array(m).fill(0))
    return bfs();
}