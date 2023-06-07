# <문제 설명>
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421

# 아래 매개변수가 주어질 때 어떤 번호가 다른 번호의 접두어인 경우가 있다면 false 그렇지 않으면 true를 반환해 주세요.
# phone_book: 전화번호부에 적힌 전화번호를 담은 배열

# <제한 사항>
# 1 <= len(phone_book) <= 1,000,000
# 각 전화번호의 길이는 1 이상 20 이하
# 같은 전화번호가 중복해서 들어있지 않습니다.

# <풀이>
# 오름차순으로 phone_book을 정렬하고
# phone_book을 순회하며 curr와 next를 비교하면 되지 않을까?
# 만약 접두사인 게 있다면 false 전부 순회했다면 true를 반환하자.
def solution(phone_book):
    pb = sorted(phone_book)
    for i in range(len(pb) - 1):
        if pb[i] == pb[i + 1][:len(pb[i])]:
            return False
    return True
