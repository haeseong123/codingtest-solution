def solution(cap, n, deliveries, pickups):
    answer = 0
    while True:
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()

        while pickups and pickups[-1] == 0:
            pickups.pop()

        if not deliveries and not pickups:
            break

        answer += max(len(deliveries), len(pickups))

        if deliveries:
            load = cap
            for i in range(len(deliveries)-1, -1, -1):
                if load >= deliveries[i]:
                    load -= deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= load
                    break

        if pickups:
            can_get = cap
            for i in range(len(pickups)-1, -1, -1):
                if can_get >= pickups[i]:
                    can_get -= pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= can_get
                    break

    return answer * 2