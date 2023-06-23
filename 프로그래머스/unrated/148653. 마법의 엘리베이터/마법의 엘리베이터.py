# -1 +1 , -10 +10, -100 +100
# 10^c (c >= 0 인 정수) 형태인 정수들이 적힌 버튼이 있습니다.
# 0 미만으로는 안움직임
# 0 층이 가장 아래층이고 엘리베이터는 현재 민수가 있는 층에 있습니다.

# 마법의 엘리베이터를 움직이기 위해서는 버튼 한 번당 마법의 돌 한 개를 사용하게 됩니다.
# 마법의 돌을 아끼기 위해 민수는 항상 최소한의 버튼을 눌러서 이동하려 합니다.
# 어떤 층에서 엘리베이터를 타고 0층으로 내려가는데 필요한 마법의 돌의 최소 개수를 구하세요.

# 아래 매개변수가 주어질 때 0층까지 가는 데 필요한 마법의 돌의 최솟값을 반환해 주세요.
# storey: 민수의 현재 층

# 어떤 자릿수의 수가 5이하일 때는 그냥 -1 하는 것이 좋다
# 왜냐하면 -1하면 5개의 마법의 돌이면 0으로 만들 수 있는데
# +1하면5개의 마법의 돌로 만들고 또 한 번 더 사용해서 올라간 자릿수를 제해야 하기 때문이다.
# 아니다. 95의 경우 +1을 다섯 번 하고 -100을 한번 하는 것이 최소다.
# 그러면 어떻게 하지?
# 각 자릿수에서 할 수 있는 것은 더하거나/빼거나 둘 중 하나이다.
#   굳이 더하면서 동시에 뺄 필요는 없다.
# 따라서 각 자릿수에서 분기를 쳐가면서 최종 수 중 최솟값을 구하는 것이 좋을 듯하다.
# 이렇게하면 각 자릿수당 2개의 분기가 발생하므로 O(2^10) 최대 이다.

# <코드>
# def (num, carry, count):
#   res = []
#   def backtrack(nums, carry, cnt):
#       if not num:
#           if carry:
#               res.append(count + 1)
#           else:
#               res.append(count)
#           return
#
#      next_carry = 0
#      if carry:
#           num[마지막] += carry
#           if num[마지막] >= 10:
#               num[마지막] -= 10
#               next_carry = 1
#
#       def(num[:마지막], next_carry, count + (num[마지막]))
#       def(num[:마지막], next_carry + 1, count + (10 - num[마지막]))
#   return res
def solution(storey):
    answers = []
    
    def calculate(num, carry, count):
        if not num:
            answers.append(count + 1 if carry else count)
            return
        num += carry
        
        calculate(num // 10, 0, count + (num % 10))
        calculate(num // 10, 1, count + (10 - (num % 10)))
    
    calculate(storey, 0, 0)
    return min(answers)