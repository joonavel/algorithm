# 연결 요소의 개수
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
from collections import deque


def bfs(k: int) -> None:
    dq = deque()
    vis[k] = True
    dq.append(k)
    
    while dq:
        now = dq.popleft()
        
        for nxt in graph[now]:
            if vis[nxt] == False:
                vis[nxt] = True
                dq.append(nxt)
            
    return



if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    vis = [False for _ in range(n + 1)]
    ans = 0
    for x in range(1, n+1):
        if vis[x] == False:
            bfs(x)
            ans += 1
    print(ans)
