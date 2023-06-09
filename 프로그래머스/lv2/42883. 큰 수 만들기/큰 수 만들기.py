# <문제 설명>
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. 
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# <제한사항>
# number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.

# <풀이>
# num은 모두 stack에 넣어야 합니다.
# 현재 num이 stack의 -1보다 크고 k가 0보다 클때
#   stack에 담긴 마지막 요소를 삭제합니다.
#   이때 1개를 삭제한 것이므로 k -= 1을 실행합니다.
#   이를 stack[-1] < num and k > 0 일때 동안 반복합니다.
# 마지막에 k != 0 이라는 것은 삭제해야 할 값이 남았다는 것입니다.
#   생각해보면 k != 0 이려면 stack에는 점점 작은값이 쌓여있다는 것입니다.
#   따라서 stack[:-k]를 하여 작은 값들을 삭제해줍니다.
# "".join(stack)을 리턴합니다.
def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)