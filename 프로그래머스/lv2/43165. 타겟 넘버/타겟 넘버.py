def solution(numbers, target):
    answer = 0
    
    def recursion(start, acc):
        nonlocal answer
        if start == len(numbers):
            if acc == target:
                answer += 1
            return
        
        recursion(start + 1, acc + numbers[start])
        recursion(start + 1, acc - numbers[start])

    recursion(0, 0)
    
    return answer
