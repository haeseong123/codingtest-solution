# result의 첫 번째 수를 x,
# num을 n이라고 할때,
# x + (x+1) + (x+2) + ... + (x+n-1) = total 을
# 만족시키는 x를 찾고
# x부터 x++ 해가며 num개만큼 반복하여 배열을 만든 후
# 해당 배열을 return하면 됩니다.
# x를 총 n번 더하니까 nx + (1 + 2 + ... + n-1) 이고
# (1 + 2 + ... + n-1) = (n-1*n)/2 이므로
# nx + (n-1*n)/2 = total 입니다.
# 우리가 구하고 싶은 것은 x 이므로 nx를 제외하고 우항으로 옮기면
# nx = total - (n-1*n)/2 이고 n으로 좌항 우항을 나누면
# x = total/n - (n-1)/2 입니다.

# 이렇게 구한 x를 총 num번 반복하여 x++해가면서 배열에 넣고
# 해당 배열을 반환하면 됩니다.

def solution(num, total):
    x = (total // num) - ((num-1) // 2)
    
    return [x+i for i in range(num)]