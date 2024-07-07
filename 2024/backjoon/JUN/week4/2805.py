# 나무 자르기
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline


def binary_search(left, right):
    
    while left <= right:
        mid = (left + right) // 2
        
        criterion = sum([tree - mid for tree in trees if tree > mid])
        
        if criterion >= m:
            left = mid + 1
        else:
            right = mid - 1
            
    return right


if __name__ == '__main__':
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    print(binary_search(0, 10 ** 9))