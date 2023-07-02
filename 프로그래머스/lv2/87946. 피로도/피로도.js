function getPermitations(arr) {
    function swap(i, j) {
        const temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    }
    
    function makePermutations(start) {
        if (start === arr.length) {
            result.push([...arr])
            return
        }

        for (let i = start; i < arr.length; i++) {
            swap(start, i);
            makePermutations(start + 1)
            swap(start, i);
        }        
    }
    
    result = []
    makePermutations(0)
    return result
}


function solution(k, dungeons) {
    function getCanEnteredDungeonsCount(d) {
        let hp = k
        let count = 0
        for (const [need, pay] of d) {
            if (hp < need) break
            hp -= pay
            count += 1
        }
    
        return count
    }
    
    let answer = 0;
    for (const dungeon of getPermitations(dungeons)) {
        answer = Math.max(answer, getCanEnteredDungeonsCount(dungeon))
    }
    return answer;
}