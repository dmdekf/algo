import sys

sys.stdin = open('input_5185.txt')
T = int(input())
# T = 1
a = ord('0')
b = ord('9')
A = ord('A')
for tc in range(1, T+1):
    N, d = map(list, input().split())
    print(d)
    result = ''
    for i in d:
        val = ord(i)
        if val > b:
            val = val - A + 10
        else:
            val = val - a

        temp = ''
        for j in range(4):
            if val & 1:
                temp = '1' + temp
            else:
                temp = '0' + temp

            val = val >> 1
        result += temp

    print(f'#{tc} {result}')
