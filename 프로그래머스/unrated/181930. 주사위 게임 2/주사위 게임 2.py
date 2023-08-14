def solution(a, b, c):
    # a != b != c
    #   a + b + c
    # 두 개는 같고 하나만 다르면
    #   ~~
    # 세개가 모두 같으면
    #   ~~
    if a != b and b != c and a != c:
        return a + b + c
    if (a == b and b != c) or (b == c and c != a) or (c == a and a != b):
        return (a + b + c) * (a**2 + b**2 + c**2)
    if a == b == c:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
