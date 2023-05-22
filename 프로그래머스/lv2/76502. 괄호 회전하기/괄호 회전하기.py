# 한 칸씩 왼쪽으로 시프트하면서
# 올바른 괄호 문자열인지 카운트하고
# 카운트한 값 반환
from collections import deque


def is_parentheses(parentheses):
    # [, (, {
    stk = []
    for p in parentheses:
        if p == '[' or p == '(' or p == '{':
            stk.append(p)
        else:
            if not stk:
                return False

            last = stk.pop()
            if p == ']' and last != '[':
                return False
            if p == ')' and last != '(':
                return False
            if p == '}' and last != '{':
                return False

    return False if stk else True


def solution(s):
    que = deque(s)
    answer = 0
    for _ in range(len(que)):
        answer += 1 if is_parentheses(que) else 0
        que.append(que.popleft())
    return answer
