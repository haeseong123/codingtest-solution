# n행 n열 2차원 배열 생성
# i = 1, ..., n에 대해 아래 과정 반복
#       1행 1열부터 i행 i열 까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
# 1행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
# 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left + 1], ... arr[right]만 남기고 지웁니다.
# n, left, right가 주어질 때 위 과정대로 만들어진 1차원 배열을 반환해주세요.
import math

def solution(n, left, right):
    ans = []

    while (left <= right):
        ans.append(max(math.floor(left / n), left % n) + 1)
        left += 1

    return ans;
