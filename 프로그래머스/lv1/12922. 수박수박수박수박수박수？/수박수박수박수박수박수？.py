def solution(n):
    value = ['수', '박']
    return ''.join([value[i%2] for i in range(n)])