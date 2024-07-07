
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    num_lst = list(map(int, input().split()))
    # 출력시 원본 수열이 필요함으로 sorted()로 분리해서 저장
    # sorted는 iterable 객체를 파라미터로 받아 list로 반환해준다.
    sorted_lst = sorted(set(num_lst))
    num_dict = {key : value for value, key in enumerate(sorted_lst)}
    print(' '.join([str(num_dict[x]) for x in num_lst]))