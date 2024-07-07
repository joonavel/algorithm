# 오등큰수
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
from collections import Counter, deque


def find_NGF():
    stack = deque()
    stack.append(0)
    for idx in range(1, n):
        # 현재 기준 오른쪽에 있으면서 가장 왼쪽에 있는 수와 비교 - idx 번째 수가 A(i)의 오등큰수인지 확인
        while stack and counter[array[stack[-1]]] < counter[array[idx]]:
            # idx 번째 수가 A(i)의 오등큰수 이면, A(i-1)의 오등큰수인지도 확인하기 위해 pop을 해준다.  
            answer[stack.pop()] = array[idx]
        # 오등큰수를 아직 찾지 못한 수들의 idx를 기록
        stack.append(idx)

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    counter = Counter(array)
    answer = [-1] * n
    find_NGF()
    print(' '.join(map(str, answer)))