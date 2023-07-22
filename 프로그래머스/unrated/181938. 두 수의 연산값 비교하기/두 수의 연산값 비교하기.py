def solution(a, b):
    answers = []
    answers.append(int(f'{a}{b}'))
    answers.append(2*a*b)
    return max(answers)