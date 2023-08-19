import heapq

def inversion(q):
    for i in range(len(q)):
        q[i] = -q[i]
    heapq.heapify(q)

def solution(operations):
    q = []
    
    for o in operations:
        command, data = o.split()
        
        if command == "I":
            heapq.heappush(q, int(data))
        else:
            if not q:
                continue
            # 최댓값 삭제
            if data == "1":
                inversion(q)
                heapq.heappop(q)
                inversion(q)
            # 최솟값 삭제
            else:
                heapq.heappop(q)
    
    if q:
        _min = q[0]
        inversion(q)
        _max = -q[0]
        return [_max, _min]
    else:
        return [0, 0]
