function solution(brown, yellow) {
    const size = brown + yellow;
    const end = Math.floor(Math.sqrt(size) + 1);
    for (let i = 3; i < end; i++) {
        if (size % i !== 0) continue
        const w = size / i
        const h = i
        if ((w - 2) * (h - 2) === yellow) return [w, h]
    }
    return [0, 0];
}