function solution(array, commands) {
    return commands.map(c => {
        const i = c[0] - 1
        const j = c[1]
        const k = c[2] - 1
        return [...array].slice(i, j).sort((a, b) => a - b)[k]
    })
}