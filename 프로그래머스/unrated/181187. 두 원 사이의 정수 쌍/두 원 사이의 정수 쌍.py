# x가 1일때 부터 r2일때 까지 모든 점의 개수를 구한 뒤
# 그것에 4를 곱한 값을 반환한다.
import math

def solution(r1, r2):
    return sum(math.floor((r2**2 - x**2)**0.5) - math.ceil(0 if r1 < x else (r1**2 - x**2)**0.5) + 1for x in range(1, r2 + 1)) << 2
