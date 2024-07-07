
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline


if __name__ == '__main__':
    n, m = map(int, input().split())
    seq = [0 for _ in range(n + 1)]
    ans = n
    temp = 1
    for _ in range(m):
        # 연결 요소가 1인 경우 나머지 정보를 볼 필요가 없다.
        if ans == 1:
            break
        # 제시된 간선이 연결 요소 정보를 갱신하는지에 대한 여부
        flag = 1
        a, b = map(int, input().split())
        
        # 두 노드에게 연결된 간선이 없을 때
        if seq[a] == 0 and seq[b] == 0:
            seq[a] = seq[b] = temp
            temp += 1
        # 한 노드만 연결된 간선이 없을 때
        elif seq[a] == 0:
            seq[a] = seq[b]
        elif seq[b] == 0:
            seq[b] = seq[a]
        
        else:
            # 이미 연결 요소인 노드끼리 연결 되었을 때
            if seq[a] == seq[b]:
                flag = 0
            # 서로 다른 연결 요소들이 연결 되었을 때
            else:
                low_seq = min(seq[a], seq[b])
                high_seq = max(seq[a], seq[b])
                for node in range(1, n+1):
                    if seq[node] == high_seq:
                        seq[node] = low_seq
                        
        # 간선 정보로 인해 연결 요소 정보가 갱신이 된 경우
        if flag:
            ans -= 1
    print(ans)