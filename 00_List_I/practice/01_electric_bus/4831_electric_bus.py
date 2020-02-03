import sys

sys.stdin = open('input.txt')

# K = 최대이동횟수
# N : 도달지점.
# M 충전기 설치 개수
# d = 충전기위치 리스트

T = int(input())
for tc in range(1,T+1):
    K , N , M = map(int, input().split())

    d = list(map(int, input().split()))

    # 출발지, 종착지를 넣어주고 해당 인터벌마다 충전소를 확인, 없는 경우 이전 충전소를 확인하는 방식으로 진행.
    d.insert(0, 0) 
    d.append(N)
    # 마지막 충전소 last, 충전횟수 cnt
    last = 0
    cnt = 0

    for i in range(1,M+2):
        if d[i] - d[i-1] > K:
            cnt = 0
            break
        if d[i] > last + K:
            last = d[i-1]
            cnt += 1 

    print('#{} {}'.format(tc, cnt))