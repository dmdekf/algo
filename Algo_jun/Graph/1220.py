def chk(i,j):

    for k in range(100):
            if d[i+k][j] == '1':
                s.append(d[i+k][j])
            else:
                if s and d[i+k][j] == '2':
                    s.pop()
                    cnt +=1
                else:
                    continue




T = 10
for tc in range(1, T+1):
    N = int(input())
    d = [list(input()) for _ in range(N)]
    cnt = 0


