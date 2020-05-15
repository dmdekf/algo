# import sys

# sys.stdin = open('input_5207.txt')

# 퀸 문제


def backtrack(idx):
    global N
    # 최종상태인지 확인하고, 최종상태이면 해
    if idx == N:
        # 다 찾았음, 해 마지막 노드 행 leaf node : 목표탐색의 마지막 구간.
        return
    # 해당 상태에서 선택할 수 있는 후보군 생성
    # 노드가 유망한지 확인 : 유망한 열, 상향대각, 하향대각
    for i in range(N):

        # if 열이 유망하고 대각들이 유망
        # 모든 후보군에 대해서 다음상태 실행
        # T = int(input())
        # for tc in range(1, T+1):
N = 4
# 각 행에는 1개의 퀸만 올 수 있음
# 열의 사용여부를 판단하는 리스트
col = [0]*N
# 대각선 유망성을 판단할 리스트
# 대각선의 개수 : N*2 -1
cnt = N*2 - 1
# 상향 : 같은 대각선의 i, j의 합이 같음.(i_j)
# 하향 : 같은 대각선의 i,j 의 차가 같음. N-(i-j)-1 == N+j-i-1
dia_1 = [0]*cnt
dia_2 = [0]*cnt
print(f'#{tc} {cnt}')
