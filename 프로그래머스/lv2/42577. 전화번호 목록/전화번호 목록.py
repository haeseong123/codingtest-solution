# <문제 설명>
# 전화번호에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421

# 아래 매개변수가 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false 그렇지 않으면 true를 반환해 주세요.
# phone_book: 전화번호부에 적힌 전화번호를 담은 배열

# <제한사항>
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
#   각 전화번호의 길이는 1 이상 20 이하입니다.
#   같은 전화번호가 중복해서 들어있지 않습니다.

# <풀이>
# phone_book을 오름차순으로 정렬하고 현재 원소와 앞의 원소를 서로 비교하여 
# 앞의 원소가 현재 원소의 접두사인지 확인한다.
def solution(phone_book):
    sorted_phone_book = sorted(phone_book)
    for i in range(1, len(sorted_phone_book)):
        if sorted_phone_book[i - 1] == sorted_phone_book[i][:len(sorted_phone_book[i - 1])]:
            return False
    return True