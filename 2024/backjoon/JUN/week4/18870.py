# 좌표 압축
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
from heapq import heappop, heapify
from typing import List, Dict

def point_compression(array: List[int]) -> Dict[int, int]:
    # 입력 받은 수열은 heap구조로 저장되어 있지 않기에 heappop전 먼저 heapify를 해주어야한다.
    heapify(array)
    temp = -1
    prev = None
    num_to_point = {}
    while array:
        now = heappop(array)
        if prev != now:
            temp += 1
        
        num_to_point[now] = temp
        prev = now
    
    return num_to_point
        
if __name__ == '__main__':
    n = int(input())
    num_heap = list(map(int, input().split()))
    ans_dict = point_compression(num_heap.copy())
    ans = [ans_dict[x] for x in num_heap]
    print(' '.join(map(str, ans)))
    