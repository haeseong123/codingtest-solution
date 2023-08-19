from functools import cmp_to_key

def comparator(a, b):
    a, b = str(a), str(b)
    c, d = int(a + b), int(b + a)
    if c > d:
        return -1
    if c == d:
        return 0
    return 1

def solution(numbers):
    return str(int("".join(list(map(str, sorted(numbers, key=cmp_to_key(comparator)))))))