// 비용 오름차순으로 비용을 정렬하고
// union-find로 연결 여부를 파악한 뒤
    // 연결되어 있지 않다면 연결하고,
    // 연결되어 있다면 넘어갑니다.
// 총 cost를 반환합니다.
class DisjointSet {
    constructor(size) {
        this.tree = Array(size).fill().map((_, i) => i)
    }
    
    find(x) {
        if (this.tree[x] === x) return x
        this.tree[x] = this.find(this.tree[x])
        return this.tree[x]
    }
    
    union(x, y) {
        x = this.find(x)
        y = this.find(y)
        
        if (x === y) return
        
        this.tree[y] = x
    }
    
    print() {
        console.log(this.tree)
    }
}

function solution(n, costs) {
    costs.sort((a, b) => a[2] - b[2])
    const d = new DisjointSet(n);
    let answer = 0
    for (const [x, y, cost] of costs) {
        if (d.find(x) === d.find(y)) continue
        d.union(x, y)
        answer += cost
    }
    return answer;
}