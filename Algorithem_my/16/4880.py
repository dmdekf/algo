# 1 가위 2 바위 3보, 1<2, 2<3, 3<1
def f(i, j):
    if i == j:
        return i
    else:
        r1 = f(i, (i+j)//2)
        r2 = f((i+j)//2+1, j)
        p = [r1, r2]
        p = [f(i, (i+j)//2), f((i+j)//2+1, j)]
        return p[w[card[r1]][card[r2]]]
        return p[w[card[f(i, (i+j)//2)]][card[f((i+j)//2+1, j)]]]
        # 값과 인덱스 값의 연동. w : 인덱스의 값으로 0또는 1(r1 == p[0], r2 == r[1])지정. 리턴할 인덱스값 반환
        # return win(r1, r2)


def win(p1, p2):
    if card[p1] == card[p2]:
        return p1
    elif card[p1] == 2 and card[p2] == 1:
        return p1
    elif card[p1] == 3 and card[p2] == 2:
        return p1
    elif card[p1] == 1 and card[p2] == 3:
        return p1
    else:
        return p2


w = [[0],           # 왼쪽 0, 오른쪽 1
     [0, 0, 1, 0],
     [0, 0, 0, 1],
     [0, 1, 0, 0]]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = [0] + list(map(int, input().split()))
    print('#{} {}'.format(tc, f(1, N)))
