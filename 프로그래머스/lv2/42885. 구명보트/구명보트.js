function solution(people, limit) {
    people.sort((a, b) => a - b)
    let left = 0,
        right = people.length - 1,
        cnt = 0
    
    while (left < right) {
        if (people[left] + people[right] <= limit) {
            left += 1
            right -= 1
            cnt += 1
        } else {
            right -= 1
            cnt += 1
        }
    }
    if (left === right) cnt += 1
    return cnt;
}