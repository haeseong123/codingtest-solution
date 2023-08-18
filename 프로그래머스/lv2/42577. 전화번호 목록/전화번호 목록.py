def solution(phone_book):
    sorted_pb = sorted(phone_book)
    for i in range(1, len(sorted_pb)):
        prev, curr = sorted_pb[i - 1], sorted_pb[i]
        if prev == curr[:len(prev)]:
            return False
    return True