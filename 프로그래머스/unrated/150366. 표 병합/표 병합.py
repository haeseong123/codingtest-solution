# 50x50 표에서 다음의 기능을 구현하려 합니다.

# 1. UPDATE r c value
#   r, c 위치의 셀을 선택합니다.
#   선택한 셀의 값을 value로 바꿉니다.

# 2. UPDATE value1 value2
#   value1을 값으로 가지고 있는 모든 셀을 선택합니다.
#   선택한 셀의 값을 value2로 바꿉니다.

# 3. MERGE r1 c1 r2 c2
#   r1, c1 위치의 셀과 r2 c2 위치의 셀을 선택하여 병합합니다.
#   선택한 두 위치의 셀이 같은 셀일 경우 무시합니다.
#   선택한 두 셀을 서로 인접하지 않을 수도 있습니다.
#       이 경우 r1, c1 위치의 셀과 r2, c2 위치의 셀만 영향을 받으며,
#       그 사이에 위치한 셀들은 영향을 받지 않습니다.
#   두 셀 중 한 셀이 값을 가지고 있을 경우 병합된 셀은 그 값을 가지게 됩니다.
#   두 셀 모두 값을 가지고 있을 경우 병합된 셀은 r1, c1 위치의 셀 값을 가지게 됩니다.
#   이후 r1, c1과 r2, c2 중 어느 위치를 선택하여도 병합된 셀로 접근합니다.

# 4. UNMERGE r c
#   r, c 위치의 셀을 선택하여 해당 셀의 모든 병합을 해제합니다.
#   선택한 셀이 포함하고 있던 모든 셀은 프로그램 실행 초기의 상태(빈 값)로 돌아갑니다.
#   병합을 해제하기 전 셀이 값을 가지고 있었을 경우 r, c 위치의 셀이 그 값을 가지게 됩니다.

# 5. PRINT r c
#   r, c 위치의 셀을 선택하여 셀의 값을 출력합니다.
#   선택한 셀이 비어있을 경우 "EMPTY"를 출력합니다.

# commands: 실행할 명령들이 담긴 1차원 문자열 배열이 주어집니다.
# commands를 순차적으로 실행하며,
# PRINT r c 명령어에 대한 실행결과를
# 배열에 담아 반환해 주세요.

# 풀이
# 명령 키워드(UPDATE, MERGE, UNMERGE, PRINT)에 맞게 각각 다른 로직을 작성하면 됩니다..
# 이를 위해 Disjoint-set을 사용하면 좋을 것 같습니다.
# 왜냐하면, 병합-병합 해제를 해야하는데, 현재 병합되어 있는지 아닌지를 파악하기에 disjoint-set이 적절한 자료구조이기 때문입니다.

# UPDATE r c value
#   => r, c의 root 노드에 있는 값을 value로 바꿉니다.
# UPDATE value1 value2
#   => 값 배열을 순회하며 value1을 전부 value2로 바꿉니다.
# MERGE r1 c1 r2 c2
#   => r1, c1과 r2, c2의 root 노드가 다를 때 아래를 실행합니다.
#       - r1, c1의 root 노드에 값이 없고 r2, c2의 루트 노드에 값이 있다면
#           r1, c1을 r2, c2에 합칩니다.
#       - 그것이 아니라면
#           r2, c2를 r1, c1에 합칩니다.
# UNMERGE r c
#   =>  1. r, c의 root 노드를 구합니다.
#       2. 모든 노드를 순회하며 해당 노드의 root노드가 1번에서 구한 root 노드와 같은지 확인합니다.
#       3. 같다면 아래를 실행합니다.
#           3-1. root노드를 현재 선택된 노드로 바꿉니다.
#           3-2. root노드의 값을 ""로 바꿉니다.
# PRINT r c
#   =>  1. r, c의 루트 노드의 value를 구합니다.
#       2. 해당 값을 answer에 넣습니다. 만약 해당 값이 ""라면 "EMPTY"를 넣습니다.

class DisjointSet:
    def __init__(self):
        self.tree = [i for i in range(50 * 50)]
        self.values = ["" for _ in range(50 * 50)]

    def update_one(self, r, c, v):
        i = self.__get_index(r, c)
        p = self.find(i)
        self.values[p] = v

    def update_all(self, v1, v2):
        for i in range(len(self.values)):
            if self.values[i] == v1:
                self.values[i] = v2

    def merge(self, r1, c1, r2, c2):
        i1, i2 = self.__get_index(r1, c1), self.__get_index(r2, c2)
        p1, p2 = self.find(i1), self.find(i2)

        if p1 == p2:
            return

        if self.values[p1] == "" and self.values[p2] != "":
            self.tree[p1] = p2
        else:
            self.tree[p2] = p1

    def unmerge(self, r, c):
        i = self.__get_index(r, c)
        p = self.find(i)
        v = self.values[p]
        unmerge_list = []

        for idx in range(len(self.tree)):
            curr_p = self.find(idx)
            if curr_p == p:
                unmerge_list.append(idx)

        for idx in unmerge_list:
            self.tree[idx] = idx
            self.values[idx] = v if idx == i else ""

    def get(self, r, c):
        i = self.__get_index(r, c)
        p = self.find(i)
        return self.values[p]

    def find(self, i):
        if self.tree[i] == i:
            return i
        else:
            return self.find(self.tree[i])

    def __get_index(self, r, c):
        return ((r - 1) * 50) + (c - 1)


def solution(commands):
    answer = []
    disjoint_set = DisjointSet()

    for cmd in commands:
        c, *args = cmd.split()
        if c == "UPDATE":
            if len(args) == 3:
                r, c, v = args
                disjoint_set.update_one(int(r), int(c), v)
            else:
                v1, v2 = args
                disjoint_set.update_all(v1, v2)
        elif c == "MERGE":
            r1, c1, r2, c2 = map(int, args)
            disjoint_set.merge(r1, c1, r2, c2)
        elif c == "UNMERGE":
            r, c = map(int, args)
            disjoint_set.unmerge(r, c)
        elif c == "PRINT":
            r, c = map(int, args)
            value = disjoint_set.get(r, c)
            answer.append("EMPTY" if value == "" else value)

    return answer
