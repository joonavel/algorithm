
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline

def operation(data: str, s: str) -> str:
    oper = data[0]
    if oper == 'empty' or oper == 'all':
        s = 0
        if oper == 'all':
            s = (1 << 21) - 1
    else:
        num = int(data[1])
        if oper == 'add':
            s |= (1 << num)
        elif oper == 'remove':
            s &= ~(1 << num)
        elif oper == 'check':
            if s & (1 << num):
                sys.stdout.write('1\n')
            else:
                sys.stdout.write('0\n')
        elif oper == 'toggle':
            s ^= (1 << num)
    return s

if __name__ == '__main__':
    m = int(input())
    s = 0
    for _ in range(m):
        data = list(input().strip().split())
        s = operation(data, s)