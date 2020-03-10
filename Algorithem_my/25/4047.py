import sys

sys.stdin = open('input.txt')
T = int(input())

dict = {'S': 0, 'C': 1, 'H': 2, 'D': 3, }
for tc in range(1, T+1):
    arr = input()
    cnt = [13]*4
    cards = set()
    for i in range(0, lne(arr), 3):
        tmp = arr[i:i+3]
        if tmp in cards:
            break
        cnt[dict[tmp[0]]] -= 1
    else:
        print(cnt)


T = int(input())
for tc in range(1, T+1):
    cards = input()
    hands = {'S': [], 'C': [], 'H': [], 'D': [], }
    for n in range(len(cards)//3):
        shape = cards[n*3]
        number = cards[n*3+1:n*3+3]
        if number not in hands[shape]:
            hands[shape].append(number)
        else:
            print('#{} ERROR'.format(tc))
            break
    else:
        result = [13-len(c) for c in hands.values()]
        print('#{} {} {} {} {}'.format(tc, *result))

T = int(input())
for tc in range(1, T+1):
    d = input()
    S = 13
    D = 13
    H = 13
    C = 13
    result = ''
    for i in range(len(d)-3+1):
        if d[i:i+3] in d[i+3:]:
            result = 'ERROR'
            break
    if result != 'ERROR':
        for i in d[::3]:
            if i == 'S':
                S -= 1
            elif i == 'D':
                D -= 1
            elif i == 'H':
                H -= 1
            elif i == 'C':
                C -= 1
        result = '{} {} {} {}'.format(S, D, H, C)

    print('#{} {}'.format(tc, result))
