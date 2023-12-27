def solution(n):
    nxt = n

    while True:
        nxt += 1
        if bin(n)[2:].count('1') == bin(nxt)[2:].count('1'):
            return nxt