def solution(s):
    answer = []
    beChanged = True
    
    for c in s:
        if c == " ":
            beChanged = True
            answer.append(c)
            continue
        
        if beChanged:
            answer.append(c.upper())
        else:
            answer.append(c.lower())
        
        beChanged = False
    
    return ''.join(answer)