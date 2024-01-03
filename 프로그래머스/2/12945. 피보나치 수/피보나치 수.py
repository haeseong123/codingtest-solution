def solution(n):
    f_arr = [0, 1, 1, 2, 3, 5]
    
    while len(f_arr) <= n:
        f_arr.append(f_arr[-1] + f_arr[-2])
        
    return f_arr[n] % 1234567