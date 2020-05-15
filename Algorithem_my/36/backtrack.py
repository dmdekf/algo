# import sys

# sys.stdin = open('input_5207.txt')

# 퀸 문제


def backtrack(idx):
    global N
    global cnt
    # 최종상태인지 확인하고, 최종상태이면 해
    if idx == N:
        # 다 찾았음, 해 마지막 노드 행 leaf node : 목표탐색의 마지막 구간.
        cnt += 1
        return
    # 해당 상태에서 선택할 수 있는 후보군 생성
    # 노드가 유망한지 확인 : 유망한 열, 상향대각, 하향대각
    for i in range(N):
        # if 열이 유망하고 대각들이 유망
        if not col[i] and not dia_1[idx+i] and not dia_2[N+i-idx-1]:
            # 모든 후보군에 대해서 다음상태 실행
            col[i] = 1
            dia_1[idx+i] = 1
            dia_2[N+i-idx-1] = 1
            backtrack(idx+1)
            col[i] = 0
            dia_1[idx+i] = 0
            dia_2[N+i-idx-1] = 0

        # T = int(input())
        # for tc in range(1, T+1):
N = 4
# 각 행에는 1개의 퀸만 올 수 있음
# 열의 사용여부를 판단하는 리스트
col = [0]*N
# 대각선 유망성을 판단할 리스트
# 대각선의 개수 : N*2 -1
dia_cnt = N*2 - 1
# 상향 : 같은 대각선의 i, j의 합이 같음.(r_c)
# 하향 : 같은 대각선의 i,j 의 차가 같음. N-(r-c)-1 == N+c-r-1
dia_1 = [0]*dia_cnt
dia_2 = [0]*dia_cnt
cnt = 0
print(f'#{tc} {cnt}')
