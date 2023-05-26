# stack을 사용하여
# 여는 괄호 "("가 나왔을 때에는 stack에 push하고
# 닫는 괄호 ")"가 나왔을 때에는 stack에 pop합니다.
#   이때 pop 할 원소가 없다면 False를 반환합니다.
# 마지막까지 왔다면 stack이 비어있으면 True를 아니라면 False를 반환합니다.
def solution(s):
    stack = []
    for x in s:
        if x == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                return False
    return False if stack else True
