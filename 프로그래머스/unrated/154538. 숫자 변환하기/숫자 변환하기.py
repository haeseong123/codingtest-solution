# x를 y로 변환하려고 합니다.
# 사용할 수 있는 연산은 다음과 같습니다.

# x에 n을 더합니다.
# x에 2를 곱합니다.
# x에 3을 곱합니다.

# 자연수 x, y, n이 매개변수로 주어질 때, 
# x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 
# 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.

# 모든 연산의 경우를 계산해보자.
# -> depth가 너무 깊어서 에러가 발생한다.
# 어떻게 계산을 줄일 수 있을까?
# bfs
from collections import deque

def solution(x, y, n):
    def bfs():
        que = deque()
        que.append(x)
        dp[x] = 1
        
        while que:
            index = que.popleft()
            
            if 0 <= index + n <= 1000000 and dp[index + n] == 0:
                dp[index + n] = dp[index] + 1
                que.append(index + n)
            if 0 <= index * 2 <= 1000000 and dp[index * 2] == 0:
                dp[index * 2] = dp[index] + 1
                que.append(index * 2)
            if 0 <= index * 3 <= 1000000 and dp[index * 3] == 0:
                dp[index * 3] = dp[index] + 1
                que.append(index * 3)
        
    dp = [0] * 1000001
    bfs()
    return dp[y] - 1