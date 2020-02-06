import sys

sys.stdin = open('input.txt')

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.

# 그 다음 M줄에는 돌을 놓을 위치와 돌의 색이 주어진다.

# 돌의 색이 1이면 흑돌, 2이면 백돌이다.

# 만약 3 2 1이 입력된다면 (3, 2) 

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    a = [[0]*N for _ in range(N)]
    a[(N//2)-1][(N//2)-1] , a[N//2][N//2] = 2, 2
    a[(N//2)-1][N//2] , a[N//2][N//2-1] = 1, 1
    # print(a)
    
    for _ in range(M):
        r, c, p = map(int, input().split())
        r -=1
        c -=1
        dx = [1, 1, 1, 0, 0, -1, -1, -1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        #black
        if p == 1:
            #중간에 [0]인 값이 없고 레인지를 벗어나지 않으며 
            temp_x = 0
            temp_y = 0
            for i in range(8):
                temp_x = r + dx[i]
                temp_y = c + dy[i]
                if -1 < temp_x < N and -1 < temp_y < N and a[temp_x][temp_y] == 2:
                    a[r][c] = 1
                # print(a)
        #white
        else:
            temp_x = 0
            temp_y = 0
            for i in range(8):
                temp_x = r + dx[i]
                temp_y = c + dy[i]
                if -1 < temp_x < N and -1 < temp_y < N and a[temp_x][temp_y] == 2:
                    a[r][c] = 2   
                # print(a)
                
    print(a)
