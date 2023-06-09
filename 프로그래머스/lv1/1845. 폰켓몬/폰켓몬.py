# <문제 설명>
# 총 N 마리의 포켓몬 중 N/2 마리를 가져가도 좋다고 했습니다.
# 숫자로 종류를 구분합니다. 예를 들어 총 4마리의 포켓몬이 있고
# 각 포켓몬의 종류 번호가 [3, 1, 2, 3]이라면 이는 3번 포켓몬 두 마리, 1번 포켓몬 한 마리, 2번 포켓몬 한 마리가 있음을 나타냅니다.
# 이때 4마리의 포켓몬 중 2마리를 고르는 방법은 다음과 같이 6가지가 있습니다.
# 1. 첫 번째(3번), 두 번째(1번) 폰켓몬을 선택
# 2. 첫 번째(3번), 세 번째(2번) 폰켓몬을 선택
# 3. 첫 번째(3번), 네 번째(3번) 폰켓몬을 선택
# 4. 두 번째(1번), 세 번째(2번) 폰켓몬을 선택
# 5. 두 번째(1번), 네 번째(3번) 폰켓몬을 선택
# 6. 세 번째(2번), 네 번째(3번) 폰켓몬을 선택

# 이때, 첫 번째(3번) 포켓몬과 네 번째(3번) 포켓몬을 선택하는 방법은 한 종류(3번 포켓몬 두 마리)의 포켓몬만 가질 수 있지만,
# 다른 방법들은 모두 두 종류의 포켓몬을 가질 수 있습니다. 따라서 위 예시에서 가질 수 있는 포켓몬 종류 수의 최댓값은 2가 돕니다.
# 당신은 최대한 다양한 종류의 포켓몬을 가지길 원하기 때문에, 최대한 많은 종류의 포켓몬을 포함해서 N/2마리를 선택하려 합니다.

# 아래 매개변수가 주어질 때 N/2 마리의 포켓몬을 선택하는 방법 중 가장 많은 종류의 포켓몬을 선택하는 방법을 찾아, 그때의 포켓몬 종류 번호의 개수를 반환해주세요.
# nums: N마리의 포켓몬의 종류 번호가 담긴 배열

# <제한사항>
# nums는 폰켓몬의 종류 번호가 담긴 1차원 배열입니다.
# nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, 항상 짝수로 주어집니다.
# 폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수로 나타냅니다.
# 가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return 하면 됩니다.

# <풀이>
# nums를 set으로 만들고 min(len(set), N//2)
def solution(nums):
    return min(len(set(nums)), len(nums) // 2)
