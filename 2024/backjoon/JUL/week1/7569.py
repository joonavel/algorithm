# 3차원 토마토
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
box = []
start_points = []
Df, Dx, Dy = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]

for f in range(h):
    filter_ = []
    for r in range(n):
        row = list(map(int, input().split()))
        filter_.append(row)
        for c, value in enumerate(row):
            if value == 1:
                start_points.append((f, r, c))
    
    box.append(filter_)
    
    
def bfs(start_points):
    # 두개의 deque을 사용함으로써 deque 교체 횟수를 통해 day를 알아낸다. 
    dq = deque()
    nxt_dq = deque()
    for point in start_points:
        dq.append(point)
    day = 0
    
    while dq or nxt_dq:
        
        if not dq:
            dq, nxt_dq = nxt_dq, deque()
            day += 1
        
        if not dq:
            day -= 1
            break
        
        f, x, y = dq.popleft()
        
        # # 방법 1
        # for df, dx, dy in zip(Df, Dx, Dy):
        #     nf, nx, ny = f + df, x + dx, y + dy
        #     if 0 <= nf < h and 0 <= nx < n and 0 <= ny < m: 
        #         if box[nf][nx][ny] == 0:
        #             box[nf][nx][ny] = 1
        #             dq.append((day + 1, (nf, nx, ny)))
        
        # 방법 2 : 방법 1의 조건식을 분해해서 더 적은 연산으로 모든 경우의 수를 확인토록 했다.
        if f > 0 and box[f - 1][x][y] == 0:
            box[f - 1][x][y] = 1
            nxt_dq.append((f - 1, x, y))
            
        if f < h - 1 and box[f + 1][x][y] == 0:
            box[f + 1][x][y] = 1
            nxt_dq.append((f + 1, x, y))
            
        if x > 0 and box[f][x - 1][y] == 0:
            box[f][x - 1][y] = 1
            nxt_dq.append((f, x - 1, y))
            
        if x < n -1 and box[f][x + 1][y] == 0:
            box[f][x + 1][y] = 1
            nxt_dq.append((f, x + 1, y))
            
        if y > 0 and box[f][x][y - 1] == 0:
            box[f][x][y - 1] = 1
            nxt_dq.append((f, x, y - 1))
            
        if y < m -1 and box[f][x][y + 1] == 0:
            box[f][x][y + 1] = 1
            nxt_dq.append((f, x, y + 1))
            
    return day


def mature_checking(array3d):
    flag = 1
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if array3d[i][j][k] == 0:
                    flag = 0
                    break
    return flag 

if mature_checking(box):
    print(0)
else:
    answer = bfs(start_points)
    
    if mature_checking(box):
        print(answer)
    else:
        print(-1)
