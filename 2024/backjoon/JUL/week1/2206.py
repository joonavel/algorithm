# 벽 부수고 이동하기
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
from collections import deque

def bfs_with_flag(grid):
    dq = deque()
    nxt_dq = deque()
    dq.append((0,0,0))
    grid[0][0] = 2
    # 시작하는 칸도 이동에 포함
    movement = 1
    while True:
        
        if not dq:
            movement += 1
            dq, nxt_dq = nxt_dq, deque()
            
        if not dq:
            return -1
        
        x, y, chance = dq.popleft()
        if x == n-1 and y == m-1:
            return movement
        
        
        for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # 미탐사 지역의 최적 경로 갱신
                if grid[nx][ny] == 0:
                    if chance == 1:
                        grid[nx][ny] = 3
                    else:
                        grid[nx][ny] = 2
                    nxt_dq.append((nx, ny, chance))
                elif grid[nx][ny] == 3:
                    if chance == 0:
                        grid[nx][ny] = 2
                        nxt_dq.append((nx, ny, chance))
                # 벽 부수고 이동하기
                elif grid[nx][ny] == 1:
                    if chance == 0:
                        # if grid[nx][ny] == 1:
                        #     grid[nx][ny] = 4
                        # else:
                        #     grid[nx][ny] = 3
                        nxt_dq.append((nx, ny, chance + 1))
                
        

if __name__ == '__main__':
    n, m = map(int, input().split())
    # 0 : 미탐사 지역, 1 : 벽, 2: 벽을 부수지 않고 도달, 3: 벽을 부수고 도달
    grid = []
    for r in range(n):
        row = list(map(int,input().strip()))
        grid.append(row)
    
    print(bfs_with_flag(grid))
    
    
# point
# 조건문의 수를 줄이거나 축약하는 것으로 시간 복잡도에서 많은 이득을 보았다.