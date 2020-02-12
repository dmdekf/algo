# example input :
# r = 4, c = 5, K = 3
# output:
# K = 3: 10
# K = 2: 10
# K = 0,1 : 20
r = 4
T = int(input())
for tc in range(1, T+1):
    c, K = map(int, input().split())
    d = [[0]*c for _ in range(r)]
    x = 0
    # Answer = 0
    while x < K:
        x +=1
        cnt = 0
        for j in range(r):
            for i in range(c):
                if not (i+j+1)%x:
                    if d[j][i]:
                        d[j][i] = 0
                    else:
                        d[j][i] = 1
                # if d[j][i]:
                    # cnt +=1
        # Answer = cnt
    Answer = sum([1 for j in range(c) for i in range(r) if d[i][j]])
    print(Answer)


