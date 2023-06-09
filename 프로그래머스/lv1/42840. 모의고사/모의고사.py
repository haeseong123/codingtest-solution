# <문제 설명>
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# <제한사항>
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

# <입출력 예>
# answers	    return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

# <문제 풀이>
# 각 수포자가 찍는 방식의 패턴을 배열에 저장해 놓습니다.
# answers를 순회하며 각 수포자가 찍는 방식의 패턴을 저장해 놓은 배열에 index로 접근하여 정답/오답 유무를 판단한 뒤,
#   corrects 배열에 저장합니다.
# corrects 배열의 max값을 구합니다.
# corrects 배열을 순서대로 순회하며 max 값과 동일한 값을 가진 원소의 (index + 1)을 answers에 추가합니다.
def solution(answers):
    corrects = [0] * 3
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i, answer in enumerate(answers):
        if answer == supo1[i % len(supo1)]:
            corrects[0] += 1
        if answer == supo2[i % len(supo2)]:
            corrects[1] += 1
        if answer == supo3[i % len(supo3)]:
            corrects[2] += 1
    
    _max = max(corrects)
    return [i + 1 for i, c in enumerate(corrects) if c == _max]
