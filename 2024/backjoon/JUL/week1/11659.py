# 구간 합 구하기 4
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
from typing import List

def get_prefix_sum(array: List[int]) -> int:
    result = [0]
    temp = 0
    for k in array:
        temp += k
        result.append(temp)
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    num_lst = list(map(int, input().split()))
    prefix_sum = get_prefix_sum(num_lst)
    for _ in range(m):
        i, j = map(int, input().split())
        print(prefix_sum[j] - prefix_sum[i-1])
    