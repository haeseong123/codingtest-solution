# my_string을 순회하며 vowel에 해당되는지 확인한다.
def solution(my_string):
    vowel = {'a', 'e', 'i', 'o', 'u'}
    return ''.join([c for c in my_string if c not in vowel])