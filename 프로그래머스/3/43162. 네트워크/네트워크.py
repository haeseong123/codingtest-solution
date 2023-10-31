def mark(group, visited, i):
    stk = [i]
    visited.add(i)

    while stk:
        curr = stk.pop()
        neighbors = group[curr]
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            stk.append(neighbor)
            visited.add(neighbor)


def solution(n, computers):
    group = [set() for _ in computers]
    for i, neighbors in enumerate(computers):
        for j, neighbor in enumerate(neighbors):
            if i == j or neighbor == 0:
                continue

            group[i].add(j)

    visited = set()
    count = 0
    for i in range(len(group)):
        if i in visited:
            continue

        mark(group, visited, i)
        count += 1

    return count
