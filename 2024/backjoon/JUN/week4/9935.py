# 문자열 폭발
import sys
sys.stdin = open('data.txt', 'r')
input = sys.stdin.readline

def explosion(string: str) -> str:
    stack = []
    length = len(bomb)
    for char in string:
        stack.append(char)
        if char == bomb[-1]:
            if ''.join(stack[-length:]) == bomb:
                del stack[-length:]
    
    if stack:
        return ''.join(stack)
    else:
        return 'FRULA'

        
if __name__ == '__main__':
    string = input().strip()
    bomb = input()
    print(explosion(string))
    
# tip

# del 은 새로운 객체를 만들지 않고, 이미 있는 객체의 내용을 바꾸는 연산이다.
# 슬라이싱으로 접근하는 방법은 매 슬라이싱마다 새로운 객체를 만들기에 적합하지 않다.
    
# python 의 문자열은 immutable 이므로 del 연산을 사용할 수 없다.

# deque는 슬라이싱 기능이 존재하지 않는다.