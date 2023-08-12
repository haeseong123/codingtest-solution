from functools import cmp_to_key

def comparator_by_asc(a, b):
    if a == 0:
        return 1
    # if b == 0:
    #     return 0
    
    a, b = str(a), str(b)
    c = int(a + b)
    d = int(b + a)
    if c > d:
        return -1
    elif c == d:
        return 0
    else:
        return 1

def solution(numbers):
    sorted_numbers = sorted(numbers, key=cmp_to_key(comparator_by_asc))
    answer = "".join(map(str, sorted_numbers)) 
    return answer if answer[0] != "0" else "0"