# <문제 설명>
# n개의 음이 아닌 정수들이 있습니다. 
# 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# 사용할 수 있는 숫자가 담긴 배열 numbers, 
# 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# <제한사항>
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

# <문제 풀이>
# 주어지는 숫자의 위치를 바꾸지 않고 적절히 더하거나 빼서 target이 되는 경우의 수를 구하는 문제입니다.
# 현재 숫자를 더하거나/빼는 두 경우를 모두 계산하면 됩니다.
# 재귀를 통해 해결하면 간단합니다.
# 재귀를 나오는 조건은 start가 len(numbers)와 같아졌을 때 입니다.
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
