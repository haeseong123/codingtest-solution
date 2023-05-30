# 투 포인터를 사용합니다.
def solution(sequence, k):
    answers = []
    l, r, acc = 0, -1, 0
    
    while True:
        if acc < k:
            r += 1
            if r >= len(sequence):
                break
            acc += sequence[r]
        else:
            acc -= sequence[l]
            l += 1
            if l == len(sequence):
                break
        
        if acc == k:
            answers.append((l, r))
            
    
    return sorted(answers, key=lambda x: (x[1] - x[0], x[0]))[0]
