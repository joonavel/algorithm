# 케빈 베이컨의 6단계 법칙
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    # 노드와 노드간의 최대 거리 : 99
    inf = 100
    graph = [[inf for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())    
        graph[a][b] = 1
        graph[b][a] = 1
        
    for k in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                if x == y:
                    graph[x][y] = 0
                    continue
                graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

    nodes = [sum(row[1:]) for row in graph[1:]]
    ans = inf * n
    for idx, value in enumerate(nodes):
        if value < ans:
            temp = idx
            ans = value
    print(temp + 1)

# 팁
# 플로이드-워셜 알고리즘은 모든 노드에 대하여 모든 노드 까지의 최단 거리를 구하는 알고리즘으로
# 시간 복잡도는 O(n^3)이다. 따라서 노드와 간선의 수가 적은 상황에서만 사용해야 한다.
