// 사각형을 그립니다.
//  테두리는 1을 넣고
//  내부는 -1을 넣습니다
//  단, -1에 1을 넣을 수는 없습니다.
//  또한 좌표가 겹칠 수 있으니 각 꼭짓점은 2배를 해줍니다.
// 마지막으로 bfs를 통해 시작점부터 목표지점까지 최단거리를 구합니다.
// 해당 최단 거리를 반환합니다.
function solution(rectangle, characterX, characterY, itemX, itemY) {
    function bfs() {
        characterX <<= 1, characterY <<= 1, itemX <<= 1, itemY <<= 1
        const que = [[characterX, characterY, 0]]
        visited[characterX][characterY] = 1
        
        while (que.length) {
            const [x, y, dist] = que.shift()
            
            if (x === itemX && y === itemY) {
                return (dist >> 1)
            }
            
            for (const [dx, dy] of moves) {
                const nx = dx + x,
                      ny = dy + y
                
                if ((0 <= nx && nx < 101) &&
                   (0 <= ny && ny < 101) &&
                   !visited[nx][ny] &&
                   matrix[nx][ny] === 1) {
                    que.push([nx, ny, dist + 1])
                    visited[nx][ny] = 1
                }
            }
        }
        
        return -1
    }
    
    // 상, 하, 좌, 우
    const moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    const matrix = Array(101).fill().map(() => Array(101).fill(0))
    const visited = Array(101).fill().map(() => Array(101).fill(0))
    for (let [x1, y1, x2, y2] of rectangle) {
        x1 <<= 1, y1 <<= 1, x2 <<= 1, y2 <<= 1
        // 좌변, 우변
        for (let ny = y1; ny <= y2; ny++) {
            if (matrix[x1][ny] === 0) {
                matrix[x1][ny] = 1            
            }
            if (matrix[x2][ny] === 0) {
                matrix[x2][ny] = 1
            }
        }
        // 밑변-윗변
        for (let nx = x1; nx <= x2; nx++) {
            if (matrix[nx][y1] === 0) {
                matrix[nx][y1] = 1
            }
            if (matrix[nx][y2] === 0) {
                matrix[nx][y2] = 1
            }
        }
        // border line을 제외한 내부는 전부 -1로 채웁니다.
        for (let nx = x1 + 1; nx < x2; nx++) {
            for (let ny = y1 + 1; ny < y2; ny++) {
                matrix[nx][ny] = -1
            }
        }
    }
    
    return bfs();
}