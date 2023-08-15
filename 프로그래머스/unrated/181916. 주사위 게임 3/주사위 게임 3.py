from collections import Counter 

def solution(a, b, c, d):
    counter = Counter([a, b, c, d])
    if len(counter) == 1:
        for k in counter.keys():
            return k * 1111
    elif len(counter) == 2:
        if max(counter.values()) == 3:
            p, q = 0, 0
            for (k, v) in counter.items():
                if v == 3:
                    p = k
                if v == 1:
                    q = k
            return (10 * p + q) ** 2
        else:
            pq = []
            for k in counter.keys():
                pq.append(k)
            return (pq[0] + pq[1]) * abs(pq[0] - pq[1])
    elif len(counter) == 3:
        answer = 1
        for (k, v) in counter.items():
            if v == 1:
                answer *= k
        return answer
    else:
        return min(counter.keys())
