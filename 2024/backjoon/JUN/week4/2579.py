# 계단 오르기
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    stairs = [0]
    for _ in range(n):
        stairs.append(int(input()))
    a = [[0 for _ in range(n+1)] for _ in range(3)]
    a[1][1] = stairs[1]
    for x in range(2, n+1):
        a[1][x] = max(a[1][x-2], a[2][x-2]) + stairs[x]
        a[2][x] = a[1][x-1] + stairs[x]
        
    print(max([x[-1] for x in a]))