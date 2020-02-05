# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스에는 N이 주어진다.

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    temp = [[0]*(N+1) for _ in range(N)]
    # print(temp)
    temp[0][1] = 1
    for i in range(1,N):
        for j in range(1,N+1):
            temp[i][j] = temp[i-1][j-1] + temp[i-1][j]
    
    print('#{}'.format(tc))
    for i in range(N):
        for x in range(1,i+2):
            print(temp[i][x],end=' ')
        print()
