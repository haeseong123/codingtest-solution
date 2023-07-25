def solution(num_list):
    odd, even = [], []
    
    for num in num_list:
        if num % 2 == 0:
            even.append(str(num))
        else:
            odd.append(str(num))
    
    return int(''.join(odd)) + int(''.join(even))