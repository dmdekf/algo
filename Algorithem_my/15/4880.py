숫자 1은 가위, 2는 바위, 3은 보를 나타낸다. 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3
def w(d):
    p = N // 2
    if len(d) ==2:
        if d[0] ==

import sys
sys.stdin = open('4880_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = list(map(int,input().split()))
    d.insert(0)
    if N%2:
        p = N // 2 + 1
    else:
        p = N // 2
