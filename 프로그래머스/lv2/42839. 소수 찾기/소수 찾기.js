function getPermutations(numbers, targetSize) {
    function makePermutations(cursor) {
        if (cursor === targetSize) {
            result.add(Number(numbers.slice(0, cursor).join('')));
            return;
        }

        for (let i = cursor; i < numbers.length; i++) {
            swap(cursor, i);
            makePermutations(cursor + 1);
            swap(cursor, i);
        }
    }
    
    function swap(i, j) {
        const temp = numbers[i];
        numbers[i] = numbers[j];
        numbers[j] = temp;
    }

    const result = new Set();
    makePermutations(0);
    return result;
}

function isPrime(num) {
    if (num <= 1) return false;
    
    const end = Math.floor(Math.sqrt(num) + 1);
    for (let i = 2; i < end; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}

function solution(numbers) {
    numbers = numbers.split('');
    let answer = 0;
    const set = new Set();
    for (let i = 1; i < numbers.length + 1; i++) {
        for (const value of getPermutations(numbers, i).values()) {
            set.add(value)
        }
    }
    for (const num of set.values()) {
        if (isPrime(num)) answer += 1;
    }
    
    return answer;
}