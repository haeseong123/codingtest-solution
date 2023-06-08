# <문제 설명>
# 아래 매개변수가 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지 반환하는 함수를 작성해 주세요.
# prices: 초 단위로 기록된 주식 가격이 담긴 배열

# <제한사항>
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

# 입출력 예
# prices	            return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

# <문제 풀이>
# prices[0]을 stack에 넣습니다.
# prices[1:]를 순회하며 아래를 수행합니다.
#   while stack[-1]의 price가 현재 price보다 클 때:
#       (현재 price의 index - stack[-1]의 idx) 를 answer[stack[-1]의 idx]에 저장합니다.
#       stack.pop()
#   현재 price를 stack에 넣습니다.
# while stack:
#   len(prices) - stack[-1]의 idx - 1을 answer[stack[-1]의 idx]에 저장합니다.
#   stack.pop()
def solution(prices):
    answer = [0] * len(prices)
    stack = [(0, prices[0])]
    
    for i, curr_p in enumerate(prices[1:]):
        curr_i = i + 1
        
        while stack and curr_p < stack[-1][1]:
            prev_i, prev_p = stack.pop() 
            answer[prev_i] = curr_i - prev_i
        stack.append((curr_i, curr_p))
    
    last_idx = len(prices) - 1
    while stack:
        prev_idx, prev_price = stack.pop()
        answer[prev_idx] = last_idx - prev_idx
        
    return answer

