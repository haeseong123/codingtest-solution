# mode 0/1
# 0
#   code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가
#   code[idx]가 "1"이면 mode를 0에서 1로 바꿈
# 1
#   code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가
#   code[idx]가 "1"이면 mode를 1에서 0으로 바꿈
def solution(code):
    mode = False
    ret = []
    for i, c in enumerate(code):
        if c == "1":
            mode = not mode
            continue
            
        isEven = i % 2 == 0
        if mode:
            if not isEven:
                ret.append(c)
        else:
            if isEven:
                ret.append(c)
                
    return "EMPTY" if not ret else "".join(ret)