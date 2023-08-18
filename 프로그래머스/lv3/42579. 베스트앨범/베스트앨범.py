def solution(genres, plays):
    dictionary = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        value = dictionary.get(g, [0, []])
        value[0] += p
        value[1].append((i, p))
        dictionary[g] = value
    sorted_album = sorted(list(dictionary.values()), key=lambda x: -x[0])
    for s_a in sorted_album:
        s_a[1].sort(key=lambda x: (-x[1], x[0]))
        
    answer = []
    for s_a in sorted_album:
        for (i, _) in s_a[1][:2]:
            answer.append(i)
    return answer