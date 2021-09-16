# 49189 가장 먼 노드
# n개의 노드와 그 사이의 간선의 정보가 주어졌을 때
# 1번 노드에서 가장 먼 노드의 갯수를 구하는 문제
# 가중치가 없는 그래프이기 때문에 단순히 bfs 로 쉽게 해결할 수 있다.


def solution(n, edge):
    # 그래프 생성
    g = [[] for _ in range(n + 1)]
    for a, b in edge:
        g[a].append(b)
        g[b].append(a)

    # 방문 여부
    visit = [False] * (n + 1)

    # 시작노드 1을 방문처리
    visit[1] = True

    # 시작 노드를 큐에 넣고 탐색 시작
    q = [1]
    while q:
        # 현재 노드들보다 먼 거리에 있는 노드의 리스트
        # q가 nq로 대체될 때 마다 시작노드로부터의 거리가 1씩 멀어진다.
        nq = []
        for node in q:
            for c in g[node]:
                if not visit[c]:
                    visit[c] = True
                    nq.append(c)

        # 현재 노드들보다 먼 노드들의 목록이 비어있는 경우
        # 현재 노드들이 가장 먼 노드들이기 때문에
        # 현재 노드 리스트의 길이를 반환
        if not nq:
            return len(q)

        q = nq
