
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline

def find_parent(k: int) -> int:
    if parents[k] != k:
        parents[k] = find_parent(parents[k])
    return parents[k]
    

def union(a: int, b: int) -> None:
    pa, pb = find_parent(a), find_parent(b)
    
    if pa > pb:
        parents[pa] = pb
    else:
        parents[pb] = pa


if __name__ == '__main__':
    n, m = map(int, input().split())
    parents = [x for x in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)
    
    roots = set([find_parent(x) for x in parents[1:]])
    print(len(roots))
    