import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{} '.format(tc))
    N = int(input())
    tmp = []
    result = [1]
    print(1)

    # temp = []일경우 for문 처음은 돌아가지 않고 temp에 result가 대입된 후 두번째행부터 포문 실행.
    for i in range(N-1):
        result = [1]
        for j in range(i):
            result.append(tmp[j]+tmp[j+1])
        result.append(1)
        print(' '.join(map(str, result)))
        tmp = result
    


