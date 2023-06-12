# numers를 순회하며 아래를 수행합니다.
#   stack에 (index, number)를 넣습니다.
#   스택의 마지막 원소보다 현재 요소가 크다면 
#   스택의 마지막 원소의 뒷 큰수는 현재 요소입니다.
#   그리고 스택의 마지막 원소보다 현재 요소가 끌 때동안 이를 반복합니다.
# stack에 남아있는 원소들은 모두 뒷 큰수가 없는 원소들입니다.
#   stack을 pop하며 해당 index에 -1을 넣습니다.
def solution(numbers):
    stack = []
    for i, number in enumerate(numbers):
        while stack and stack[-1][1] < number:
            prev_i, _ = stack.pop()
            numbers[prev_i] = number
        stack.append((i, number))
        
    while stack:
        prev_i, _ = stack.pop()
        numbers[prev_i] = -1
        
    return numbers
