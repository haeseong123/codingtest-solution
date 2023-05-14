# numbers를 순회하며 해당 숫자를 더하거나 빼거나 하는 
# 경우를 모두 고려하여 target이 되면 누적합니다.
def solution(numbers, target):
    n = len(numbers)

    def backtrack(curr_sum, index):
        if index >= n:
            return 1 if curr_sum == target else 0

        return backtrack(curr_sum + numbers[index], index + 1) + backtrack(curr_sum - numbers[index], index + 1)

    return backtrack(0, 0)  