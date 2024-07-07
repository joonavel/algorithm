# 2 x n 타일링
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def solution(k):
    if n <= 1:
        return 1
    if dp[k] > 0:
        return dp[k]
    dp[k] = solution(k-1) + solution(k-2)
    return dp[k]


if __name__ == '__main__':
    n = int(input())
    dp = [1, 1] + [0] * 999
    print(solution(n))
    
    