import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    d = [list(input().split()) for _ in range(N)]

    cntl = []
    col_d = []
    for i in range(N):
        col = ''
        for j in range(N):
            col += d[j][i]
        col_d.append(list(col))
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if d[i][j] == '1':
                cnt +=1                   
            if d[i][j] == '0' and cnt !=0:
                if M == cnt:
                    result +=1
                    cnt = 0
            if j == N-1:
                if M == cnt:
                    result +=1

    for i in range(N):
        cnt = 0
        for j in range(N):
            if col_d[i][j] == '1':
                cnt +=1                   
            if col_d[i][j] == '0' and cnt !=0:
                if M == cnt:
                    result +=1
                    cnt = 0
            if j == N-1:
                if M == cnt:
                    result +=1
    
    print('#{} {}'.format(tc, result))
