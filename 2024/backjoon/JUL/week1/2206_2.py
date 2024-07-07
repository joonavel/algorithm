
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
from collections import deque
from typing import List, Optional

def shortest_path(N: int, M: int, matrix: List[str]) -> Optional[int]:
    # 거리 행렬을 -1로 초기화 - 아직 한번도 방문하지 않은 상태
    # z : 0이면 벽을 부수지 않음, 1이면 벽을 부숨
    distances = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(2)]
    # deque 생성
    queue = deque()
    # 시작점 추가
    queue.append((0, 0, 0))
    # 거리 행렬의 시작점을 1로 갱신
    distances[0][0][0] = 1
    # 4방향 움직임을 미리 구현
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        # z : 벽을 부수지 않은 상태 - 0, 벽을 부순 상태 - 1
        x, y, z = queue.popleft()
        if x == N-1 and y == M-1:
            return distances[z][x][y]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == '0' and distances[z][nx][ny] == -1:
                    distances[z][nx][ny] = distances[z][x][y] + 1
                    queue.append((nx, ny, z))
                elif z == 0 and matrix[nx][ny] == '1' and distances[1][nx][ny] == -1:
                    distances[1][nx][ny] = distances[z][x][y] + 1
                    queue.append((nx, ny, 1))
    return -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [list(input()) for _ in range(n)]
    print(shortest_path(n, m, matrix))