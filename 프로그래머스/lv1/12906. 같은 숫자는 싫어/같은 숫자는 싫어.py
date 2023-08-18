def solution(arr):
    answer = [arr[0]]
    for e in arr[1:]:
        if answer[-1] != e:
            answer.append(e)
    return answer
