# 이분 그래프
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
from collections import deque


def bfs(k: int) -> bool:
    dq = deque()
    nxt_dq = deque()
    dq.append(k)
    team = identity[k]
    while True:
        
        if not dq:
            dq, nxt_dq = nxt_dq, deque()
            # 0 -> 1, 1 -> 0
            team = (team + 1) % 2
        
        if not dq:
            return True
        
        now = dq.popleft()
        nxt_team = (team + 1) % 2
        for nxt in graph[now]:
            # 방문할 노드의 팀이 아직 정해지지 않은 경우
            if identity[nxt] < 0:
                # now의 팀과 다른팀을 지정
                identity[nxt] = nxt_team
                nxt_dq.append(nxt)
            # 방문할 노드의 팀이 이미 정해져있는 경우
            else:
                # 현재 노드와 같은 팀이었던 경우
                if identity[nxt] == team:
                    return False
                # 현재 노드와 다른 팀인 경우
                else:
                    pass
                    

if __name__ == '__main__':
    cases = int(input())
    
    for case in range(cases):
        v, e = map(int, input().split())
        # 각 노드가 속한 팀 - -1 : 미정, 0: 1팀, 1 : 2팀
        identity = [-1 for _ in range(v + 1)]
        graph = [[] for _ in range(v + 1)]
        for _ in range(e):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        
        for node in range(1, v+1):
            if identity[node] < 0:
                if node == 1:
                    identity[1] = 0
                if not bfs(node):
                    print('NO')
                    break
        if node == v:
            print('YES')
        
        
        