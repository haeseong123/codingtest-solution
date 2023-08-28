# 카카오 프렌즈를 두 팀으로 나누고, 각 팀이 같은 곳을 다른 순서로 방문하도록 해서 먼저 순회를 마친 팀이 승리
# 규칙
#   트리를 구성하는 모든 노드의 x, y 좌표 값은 정수이다.
#   모든 노드는 서로 다른 x값을 가진다.
#   같은 레벨에 있는 노드는 같은 y 좌표를 가진다.
#   자식 노드의 y 값은 항상 부모 노드보다 작다.
#   임의의 노드 V의 왼쪽 서브 트리에 있는 모든 노드의 x값은 V의 x값보다 작다.
#   임의의 노드 V의 오른쪽 서브 트리에 있는 모든 노드의 x값은 V의 x값보다 크다.

# 이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo가 매개변수로 주어질 때,
# 노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과를 2차원 배열에 순서대로 담아 return 하도록 solution 함수를 완성하자.

# <제한사항>
#   nodeinfo는 이진트리를 구성하는 각 노드의 좌표가 1번 노드부터 순서대로 들어있는 2차원 배열이다.
#       nodeinfo의 길이는 1이상 10,000 이하이다.
#       nodeinfo[i]는 i + 1번 노드의 좌표이며, [x축 좌표, y축 좌표] 순으로 들어있다.
#       모든 노드의 좌표 값은 0이상 100,000 이하인 정수이다.
#       트리의 깊이가 1,000 이하인 경우만 입력으로 주어진다.
#       모든 노드의 좌표는 문제에 주어진 규칙을 따르며, 잘못된 노드 위치가 주어지는 경우는 없다.

# <문제 풀이>
#   1. nodeinfo를 트리로 만들어야 함
#       for i, n in enumerate(nodeinfo): n.append(i + 1)
#       y 값 내림차순, x 값 오름차순
#   2. answer.append(전위 순회())
#   3. answer.append(후위 순회())
#   4. return answer
import sys
sys.setrecursionlimit(10**6)

def preorder(arrY, arrX, answer):
    node = arrY[0]
    idx = arrX.index(node)
    arrY1 = []
    arrY2 = []
    
    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])
    
    answer.append(node[2])
    if len(arrY1) > 0:
        preorder(arrY1, arrX[:idx], answer)
    if len(arrY2) > 0:
        preorder(arrY2, arrX[idx + 1:], answer)
    return

def postorder(arrY, arrX, answer):
    node = arrY[0]
    idx = arrX.index(node)
    arrY1 = []
    arrY2 = []
    
    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])
    
    if len(arrY1) > 0:
        postorder(arrY1, arrX[:idx], answer)
    if len(arrY2) > 0:
        postorder(arrY2, arrX[idx + 1:], answer)
    answer.append(node[2])
    return

def solution(nodeinfo):
    preanswer = []
    postanswer = []
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    arrY = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))
    arrX = sorted(nodeinfo)
    
    preorder(arrY, arrX, preanswer)
    postorder(arrY, arrX, postanswer)
    
    return [preanswer, postanswer]



