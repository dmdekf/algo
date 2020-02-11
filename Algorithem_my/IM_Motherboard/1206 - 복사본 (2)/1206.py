import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, 11):
    num = int(input())
    building = list(map(int, input().split()))
    count = 0

    for i in range(2, num - 2):
        if building[i] - building[i - 1] >= 1 and building[i] - building[i - 2] >= 1 and building[i] - building[
            i + 1] >= 1 and building[i] - building[i + 2] >= 1:
            temp = [building[i] - building[i - 1], building[i] - building[i - 2], building[i] - building[i + 1],
                    building[i] - building[i + 2]]
            count += min(temp)
    print(f'#{tc} {count}')




