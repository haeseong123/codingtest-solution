# 1. `answer` 변수를 생성하고 0을 넣습니다.
# 2. 주어진 `numbers`를 리스트로 변환합니다.
# 3. nPr에서 모든 r에대한 순열을 생성하도록 1부터 len(numbers)까지 반복합니다.
# 4. i를 넣어 `permutations(numbers, i)`를 호출합니다.
# 5. 생성된 순열의 요소가 소수인지 확인합니다. 만약 소수라면 `answer += 1`을 합니다.
# 6. `answer`를 반환합니다.


# 소수를 판별하는 함수입니다.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 순열을 생성하는 함수입니다.
def permutations_recursion(arr, r):
    result = set()  # 중복을 피하기 위해 set을 사용합니다.
    n = len(arr)

    def backtrack(start):
        if start == r:
            # 맨 앞자리가 0이면 숫자로 바꿀 때 자릿수가 
            # 줄어드므로 result에 추가하지 않습니다.
            if arr[0] != '0':
                result.add(int(''.join(arr[:r])))
            return
        for i in range(start, n):
            arr[start], arr[i] = arr[i], arr[start]  # 자리 바꾸기
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]  # 자리 원위치

    backtrack(0)
    return result


def solution(numbers):
    answer = 0
    numbers = list(numbers)

    # nPr에서 모든 r에대한 순열을 생성하도록 1부터 len(numbers)까지 반복합니다.
    for i in range(1, len(numbers) + 1):
        # 순열을 생성합니다. P(numbers, 1), P(numbers, 2), ..., P(numbers, n)
        for p in permutations_recursion(numbers, i):
            # 생성된 순열이 소수인지 판별합니다.
            if is_prime(p):
                answer += 1

    return answer
