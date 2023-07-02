// 해당 수를 더하거나/빼거나 두 가지를 분기로 처리

function solution(numbers, target) {    
    function recursion(sum, index) {
        if (index === numbers.length) {
            if (sum === target) answer += 1
            return
        }
        
        recursion(sum + numbers[index], index + 1)
        recursion(sum - numbers[index], index + 1)
    }
    
    let answer = 0;
    recursion(0, 0);
    return answer;
}