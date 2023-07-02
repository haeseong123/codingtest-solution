function solution(numbers) {
    const answer =  numbers.sort((a, b) => {
        a = String(a)
        b = String(b)
        
        if (a + b < b + a) {
            return 1;
        } else if (a + b == b + a) {
            return 0;
        } else {
            return -1;
        }
    }).join('')
    
    return answer[0] === '0' ? '0' : answer
}