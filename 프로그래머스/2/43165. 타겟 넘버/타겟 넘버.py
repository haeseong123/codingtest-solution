def solution(numbers, target):
    answer = 0

    def recursion(curr_sum, idx):
        nonlocal answer
        if idx >= len(numbers):
            if curr_sum == target:
                answer += 1
            return

        recursion(curr_sum + numbers[idx], idx + 1)
        recursion(curr_sum - numbers[idx], idx + 1)

    recursion(0, 0)
    
    return answer
