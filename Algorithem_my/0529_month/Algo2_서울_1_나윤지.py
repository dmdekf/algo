
import sys

sys.stdin = open('2input.txt')


def f(v, cnt, M, temp):
    global result
    if temp > result:
        result = temp
    if cnt == M:
        return
    for i in range(len(v)):
        for j in range(i+1, len(node)):
            if v[i] == 0 and node[j][i] == 0:
                v[i] = 1
                node[j][i] = 1
                f(v, cnt + 1, M, temp + 1)
                v[i] = 0
                node[j][i] = 0


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 각 어린이별 가질 수 있는 사탕의 종류 행렬만들기
    node = [[0]*M for _ in range(N)]
    v = [0 for _ in range(M)]
    # 각 어린이 별 가지고 있는 사탕의 개수와 총합 개수
    for i in range(N):
        temp = []
        temp = list(map(int, input().split()))
        for j in range(temp[0]):
            node[i][temp[j]-1] = 1

    # 나눠주기 전 사탕 종류 값
    # print(sum(sum(i) for i in node))
    result = sum(sum(i) for i in node)
    f(v, 0, M, result)
    print(f'#{tc} {result}')
