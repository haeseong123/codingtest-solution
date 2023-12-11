def solution(s):
    trans_count, removed_count = 0, 0
    
    while s != '1':
        zero_count = s.count('0')
        one_count = len(s) - zero_count

        s = str(format(one_count, 'b'))
        
        trans_count += 1
        removed_count += zero_count
            
    
    return [trans_count, removed_count]