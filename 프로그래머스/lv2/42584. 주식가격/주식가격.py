def solution(prices):
    stack = [(0, prices[0])]
    answer = [0] * len(prices)
    for i in range(1, len(prices)):
        if not stack:
            stack.append((i, prices[i]))
            continue
        
        if stack[-1][1] <= prices[i]:
            stack.append((i, prices[i]))
        else:
            while stack and stack[-1][1] > prices[i]:
                s_i, s_p = stack.pop()
                answer[s_i] = i - s_i
            stack.append((i, prices[i]))
            
    while stack:
        s_i, s_p = stack.pop(0)
        
        if stack:
            answer[s_i] = stack[-1][0] - s_i
        else:
            answer[s_i] = 0
            
    return answer