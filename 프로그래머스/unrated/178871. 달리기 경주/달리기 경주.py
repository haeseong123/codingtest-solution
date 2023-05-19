# 이름이 불린 player를 찾아서 앞에 위치한 player와 자리를 바꿔주자.
# 이중 for문으로 문제를 풀면 시간초과가 발생하므로,
# map과 함께 사용하자

def solution(players, callings):
    # rank = {내 이름: 내 위치}
    rank = {players[i]: i for i in range(len(players))}
    for name in callings:
        # name에 해당되는 사람의 인덱스를 rank에서 찾는다. O(1)
        # 내 위치를 통해서 나와 내 앞의 사람을 바꾼다. O(1)
        # 내 앞의 사람의 위치를 +1한다. O(1)
        # 내 위치를 -1한다. O(1)
        here = rank[name]
        rank[players[here - 1]] += 1
        rank[name] -= 1
        players[here - 1], players[here] = players[here], players[here - 1]
    return players