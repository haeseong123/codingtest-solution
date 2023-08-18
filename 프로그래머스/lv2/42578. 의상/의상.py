def solution(clothes):
    # 이름, 종류
    dictionary = {}
    for name, _type in clothes:
        value = dictionary.get(_type, [])
        value.append(name)
        dictionary[_type] = value
    
    answer = 1
    for k in dictionary.values():
        answer *= (len(k) + 1)
    return answer - 1