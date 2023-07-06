function solution(num_list, n) {
    return num_list.filter((e, i) => {
        if (i === 0 || i % n === 0) return true
        return false
    });
}