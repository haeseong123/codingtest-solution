# s를 순회하며
# stack의 마지막 요소와 현재 넣으려는 요소가 다를 때만 stack에 추가합니다.
def solution(s):
    answer = [s[0]]
    for n in s[1:]:
        if answer[-1] == n: 
            continue
        answer.append(n)
    return answer
