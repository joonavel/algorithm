# 리모컨
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline


def solution(target, current):
    # 모든 경우의 수를 탐색한 경우
    if len(target) == len(current):
        return abs(int(target) - int(current)) + len(target)
    
    # 현재 목표로하는 채널의 특정 자리수
    now = target[len(current)]
    
    # 고장나지 않아 바로 접근이 가능한 경우
    if not int(now) in broken:
        temp_ans = solution(target, current + now)
    # 고장나서 크거나 작은 숫자로 우회해야하는 경우
    else:
        temp_ans = sys.maxsize

    # 현재 자리수보다 큰 수들의 모임과 작은 수들의 모임
    higher = [x for x in available if int(now) < int(x)]
    lower = [x for x in available if int(now) > int(x)]
    # 특정 자리수가 목표보다 큰 것중 가장 작은 수
    if higher:
        high = current + str(min(higher)) + (min_num * (len(target) - len(current) - 1))
    else:
        high = str(sys.maxsize)
    # 특정 자리수가 목표보다 작은 것중 가장 큰 수
    if lower:
        low = current + str(max(lower)) + (max_num * (len(target) - len(current) - 1))
    else:
        low = str(sys.maxsize)
    
    high_ans = abs(int(high) - int(target)) + len(high)
    low_ans = abs(int(low) - int(target)) + len(low)
    # 최소 경로 반환하기
    return min(high_ans, low_ans, temp_ans)
    
if __name__ == '__main__':
    target = input().strip()
    broken_cnt = int(input())
    # 모든 번호가 고장 났다면 solution 함수를 쓸 필요가 없다
    if broken_cnt == 10:
        broken = set(map(int, input().split()))
        temp_ans = sys.maxsize
        high_ans = sys.maxsize
        low_ans = sys.maxsize
    else:
        # 고장난 번호가 없다면 3번째 입력 값이 없다
        if broken_cnt == 0:
            broken = set()
        else:
            broken = set(map(int, input().strip().split()))
    
        # 사용 가능한 숫자
        available = [x for x in range(10) if not x in broken]
        min_num = str(min(available))
        max_num = str(max(available))
        
        temp_ans = solution(target, '')

        # 특이 케이스 처리
        # 숫자가 0 밖에 안남았는데 target은 두자리 숫자 이상인 경우
        if min_num == '0' and len(available) == 1:
            high = '0'
        # 더 큰 자리수의 최소 채널에서 비교하기
        elif min_num == '0':
            nonzero = str(min(x for x in available if x != 0))
            high = nonzero + '0' * len(target)
        else:
            high = min_num * (len(target) + 1)
        # 더 작은 자리수의 채널에서 비교하기
        if len(target) != 1:
            low = max_num * (len(target) - 1)
        else:
            low = max_num

        high_ans = abs(int(high) - int(target)) + len(high)
        low_ans = abs(int(low) - int(target)) + len(low)
    
    # 채널 100번에서 + 또는 -로 이동하는 것과 비교해야한다
    start100_ans = abs(int(target) - 100)
    ans = min(temp_ans, start100_ans, high_ans, low_ans) 
    print(ans)