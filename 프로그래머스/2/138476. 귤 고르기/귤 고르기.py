from collections import Counter

def solution(k, tangerine):
    answer = 0
    for (size, count) in Counter(tangerine).most_common():
        k -= count
        answer += 1
        
        if k <= 0:
            break
            
    return answer