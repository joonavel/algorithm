# 쉬운 최단거리
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
from collections import deque

def bfs(i, j):
    dq = deque()
    nxt_dq = deque()
    dq.append((i, j))
    temp = 1
    
    while True:
        
        if not dq:
            dq, nxt_dq = nxt_dq, deque()
            temp += 1
        
        if not dq:
            return

        x, y = dq.popleft()
        
        if x > 0 and grid[x - 1][y] == 1:
            grid[x - 1][y] = 2
            ans[x-1][y] = temp
            nxt_dq.append((x-1, y))
        if x < n - 1 and grid[x + 1][y] == 1:
            grid[x + 1][y] = 2
            ans[x+1][y] = temp
            nxt_dq.append((x+1, y))
        if y > 0 and grid[x][y - 1] == 1:
            grid[x][y - 1] = 2
            ans[x][y-1] = temp
            nxt_dq.append((x, y-1))
        if y < m - 1 and grid[x][y + 1] == 1:
            grid[x][y + 1] = 2
            ans[x][y+1] = temp
            nxt_dq.append((x, y+1))

if __name__ == '__main__':
    n, m = map(int, input().split())
    grid = []
    ans = [[0 for _ in range(m)] for _ in range(n)]    
    for r in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
        for c, value in enumerate(row):
            if value == 2:
                start_x, start_y = r, c

    bfs(start_x, start_y)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                ans[i][j] = -1
    for ans_row in ans:
        print(' '.join(map(str, ans_row)))