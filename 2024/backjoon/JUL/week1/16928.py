# 뱀과 사다리 게임
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
from collections import deque


def bfs(ladders, snakes):
    dq = deque()
    nxt_dq = deque()
    dq.append(1)
    movement = 0
    while dq or nxt_dq:
        
        if not dq:
            dq, nxt_dq = nxt_dq, deque()
            movement += 1

        now = dq.popleft()
        default = 0
        for dx in range(1, 7):
            nxt = now + dx
            
            if nxt == 100:
                return movement + 1
            elif nxt > 100:
                continue
            
            if nxt in ladders:
                nxt_dq.append(ladders[nxt])
            elif nxt in snakes:
                nxt_dq.append(snakes[nxt])
            else:
                default = nxt
        if default:
            nxt_dq.append(default)
                
    return movement


if __name__ == '__main__':
    n, m = map(int, input().split())
    ladders = {}
    snakes = {}
    
    for _ in range(n):
        start, end = map(int, input().split())
        ladders[start] = end
    
    for _ in range(m):
        start, end = map(int, input().split())
        snakes[start] = end
    
    print(bfs(ladders, snakes))
    
        