def solution(sequence):
    for (i, s) in enumerate(sequence):
        if i % 2 == 1:
            sequence[i] = -sequence[i]

    l = len(sequence)
    dp = [[0 for _ in range(l)] for _ in range(2)]
    dp[0][0] = sequence[0]
    dp[1][0] = -sequence[0]

    for (i, s) in enumerate(sequence[1:]):
        dp[0][i + 1] = max(dp[0][i] + s, s)
        dp[1][i + 1] = max(dp[1][i] - s, -s)

    return max(max(dp[0]), max(dp[1]))