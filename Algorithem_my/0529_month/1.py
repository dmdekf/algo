
import sys

sys.stdin = open('input.txt')

def f(row,col,num):
    global Flag
    if Flag == False:
        return
    for i in range(9):
        # 입력할 값에 대한 행렬이 0이아니거나 대입할 숫자가 행과 열에 있다면 시도를 멈춘다.(Flag = False)
        if d[row][col] != 0 or d[row][i] == num or d[i][col] == num:
            Flag = False
            return
    if row == 0:
        x = 0
    else:
        x = row//3
    if col == 0:
        y = 0
    else:
        y = col//3
    # 3X3 크기의 작은 격자 안에서 판별하기.
    for j in range(3):
        for k in range(3):
            if d[x*3 + j][y*3 + k] == num:
                Flag = False
                return
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 입력된 데이타를 행렬값으로 저장.
    d = [list(map(int,input().split())) for _ in range(9)]
    Flag = True
    cnt = 0
    # 시도횟수 N번 중
    for _ in range(N):
        #row, col, num 값을 각각 저장
        row, col, num = map(int,input().split())
        #스도쿠 행렬에서 값이 대입할 수 있는지 시도한다.
        f(row,col,num)
        # Flag가 참이면 cnt를 하나씩 증가시키고 행렬에 num값을 대입, 계속 게임 진행
        if Flag:
            d[row][col] = num
            cnt+=1

    print(f'#{tc} {cnt}')
