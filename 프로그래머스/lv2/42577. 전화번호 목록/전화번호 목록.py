# 1. phone_book을 정렬하고
# 2. i번째 숫자가 i+1의 접두어인지 확인한다.
#       접두어라면 false를 반환한다.
# 3. true를 반환한다.
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
            return False
    return True
