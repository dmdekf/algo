# 3
# 3 5 6 5
# 2 3 1 8 9
# 7 6 2 2 6
# # 5 7 3 8 7
# # 구역의 크기 N, M, 높이제한 K, H가 차례로 주어지고, 다음 줄부터 N줄에 걸쳐, M개 씩의 높이
import sys

sys.stdin = open('input_9476.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K, H = map(int, input().split())
    d = [list(map(int,input().split())) for _ in range(N)]

    chk = True
    cnt = 0
    for i in range(N-3+1):
        for j in range(M-3+1):
            maxd = -1
            mind = 98765
            for l in range(3):
                for k in range(3):
                    if (i+l,j+k) != (i+1,j+1):
                        if maxd <d[i+l][j+k]:
                            maxd = d[i+l][j+k]
                        if mind > d[i+l][j+k]:
                            mind = d[i+l][j+k]
            if maxd - mind > K or d[i+1][j+1] < mind or d[i+1][j+1] - mind > H:
                continue
            cnt +=1
    print(cnt)




