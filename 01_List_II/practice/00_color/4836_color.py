import sys

sys.stdin = open('input.txt')

# 1. 10 x 10  격자를 생성
# 2. input으로 주어진 조건에 따라 색칠
# - 왼쪽 상단 인덱스 & 오른쪽 하단 인덱스
# 3. 겹쳐진 구간의 개수 출력(cnt)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    #이중배열 초기화. [[0]*n]*n은 쓰지 않기. 값이 변하면 모두 복제됨.
    # 같은 색이 중복으로 될 경우 set으로 접근해보기.
    tile = [[0]*10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        #x축의 범위
        for i in range(r1, r2+1):
            #y축의 범위
            for j in range(c1, c2+1):
                tile[i][j] += color 
                if tile[i][j] == 3:
                    cnt +=1
    
    print('#{} {}'.format(tc, cnt))
