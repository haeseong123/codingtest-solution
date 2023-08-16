from functools import reduce

def solution(num_list):
    multiple = reduce(lambda acc, num: acc * num, num_list, 1)
    sum_square = sum(num_list) ** 2
    
    return 1 if multiple < sum_square else 0
