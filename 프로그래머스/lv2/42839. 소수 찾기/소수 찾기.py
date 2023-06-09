# <문제 설명>
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# <제한사항>
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

# <문제 풀이>
# 순열(Permutation)을 사용하여 주어진 numbers로 만들 수 있는 모든 정수를 갖는 배열을 구합니다.
# 배열을 순회하며 해당 정수가 소수인지 판별하고 소수가 맞다면 answer에 +1을 합니다.
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    answer = 0
    ps = set()
    
    def permutations(start, r):
        if start == r:
            ps.add(int("".join(numbers[:r])))
            return
        
        for i in range(start, len(numbers)):
            numbers[start], numbers[i] = numbers[i], numbers[start]
            permutations(start + 1, r)
            numbers[start], numbers[i] = numbers[i], numbers[start]
    
    for i in range(1, len(numbers) + 1):
        permutations(0, i)
    
    for p in ps:
        if is_prime(p):
            answer += 1
    
    return answer
    