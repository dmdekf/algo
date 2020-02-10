import sys
sys.stdin = open('input.txt')
def ch(word):
    if word == word[::-1]:
        return True
    return False
T = 10
for tc in range(1, T+1):
    N = 8
    n = int(input())
    d = [list(input()) for _ in range(N)]
    cold = []
    for i in range(N):
        temp = ''
        for j in range(N):
            temp +=d[j][i]
        cold.append(temp)
    cnt = 0
    for i in range(N):
        for j in range(N-n+1):
            if ch(d[i][j:j+n]):
                cnt +=1
            if ch(cold[i][j:j+n]):
                cnt +=1
    print('#{} {}'.format(tc, cnt))
