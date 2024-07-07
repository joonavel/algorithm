# 계단 오르기
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline


def solution(k):    
    dp = [0 for _ in range(n+1)]
    dp[1] = stairs[1]
    if k >= 2:
        dp[2] = stairs[1] + stairs[2]
    for x in range(3, n+1):
        dp[x] = max(dp[x-2] + stairs[x], dp[x-3] + stairs[x-1] + stairs[x])
    return dp[-1]

if __name__ == '__main__':
    n = int(input())
    stairs = [0]
    for _ in range(n):
        stairs.append(int(input()))
    
    print(solution(n))