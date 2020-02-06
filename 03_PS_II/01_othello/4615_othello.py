import sys

sys.stdin = open('input.txt')

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.

# 그 다음 M줄에는 돌을 놓을 위치와 돌의 색이 주어진다.

# 돌의 색이 1이면 흑돌, 2이면 백돌이다.

# 만약 3 2 1이 입력된다면 (3, 2)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = [[0]*N for _ in range(N)]
    a[(N//2)-1][(N//2)-1] = a[N//2][N//2] = 2
    a[(N//2)-1][N//2] = a[N//2][N//2-1] = 1
    # print(a)

    for _ in range(M):
        c, r, p = map(int, input().split())
        r -= 1
        c -= 1
        dx = [0, 0, -1, 1, -1, 1, -1, 1]
        dy = [-1, 1, 0, 0, -1, -1, 1, 1]
        # black

        if p == 1:
            another = 2
        else:
            another = 1
        a[r][c] = p
        # 중간에 [0]인 값이 없고 레인지를 벗어나지 않으며

        for i in range(8):
            temp_x = r + dx[i]
            temp_y = c + dy[i]
            if 0 <= temp_x < N and 0 <= temp_y < N:
                if a[temp_x][temp_y] == another:
                    cnt = 0
                    while a[temp_x][temp_y] == another:
                        temp_x = temp_x + dx[i]
                        temp_y = temp_y + dy[i]
                        cnt += 1
                        if temp_x < 0 or temp_x >= N or temp_y < 0 or temp_y >= N or a[temp_x][temp_y] == 0:
                            cnt = 0
                            break
                    temp_x = r + dx[i]
                    temp_y = c + dy[i]

                    while cnt != 0:
                        print(temp_y, temp_x, r, c, cnt)
                        a[temp_x][temp_y] = p
                        temp_x = temp_x + r
                        temp_y = temp_y + c
                        cnt -= 1
        black = 0
        white = 0
        for i in range(N):
            for j in range(N):
                if a[i][j] == 1:
                    black += 1
                elif a[i][j] == 2:
                    white += 1
    print('#{} {} {}'.format(tc, black, white))
