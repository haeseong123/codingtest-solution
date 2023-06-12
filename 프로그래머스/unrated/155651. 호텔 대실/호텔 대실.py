# 우선 book_time을 입실 시간 기준 오름차순으로 정렬합니다.
# book_time을 순회하며 아래를 수행합니다.
#   최소힙(퇴실 시간 기준 최소힙)에 마지막 원소를 뽑습니다.
#   만약 최소힙의 마지막 원소 + 10 보다 현재 book_time의 원소가 더 크다면:
#       방이 하나 더 필요한 것이므로 answer += 1을 수행합니다.
#       최소힙의 마지막 원소를 다시 최소힙에 넣습니다.
#   현재 book_time의 퇴실 시간을 최소힙에 넣습니다.
# answer를 반환합니다.
import heapq

def solution(book_time):
    def str2m(s):
        hh, mm = map(int, s.split(":"))
        return (hh * 60) + mm
        
    def update_room(now):
        # 쫓아낼 손님 쫓아내기
        while heap and heap[0] <= now:
            heapq.heappop(heap)
        
    def has_empty_room():
        # 빈방 있는지 확인하기
        return len(heap) < capacity
    
    capacity = 0
    heap = []
    for it, ot in sorted(book_time):
        now, out_time = str2m(it), str2m(ot) + 10
        update_room(now)
        
        if not has_empty_room():
            capacity += 1
        
        heapq.heappush(heap, out_time)
        
    return capacity