def solution(topping):
    answer = 0
    l, r = dict(), dict()

    for t in topping:
        value = r.get(t)

        if value:
            r[t] += 1
        else:
            r[t] = 1

    for t in topping:
        value = l.get(t)

        if value:
            l[t] += 1
        else:
            l[t] = 1

        r[t] -= 1
        if r[t] == 0:
            r.pop(t)

        if len(l) == len(r):
            answer += 1

    return answer