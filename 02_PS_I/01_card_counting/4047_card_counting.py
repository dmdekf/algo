import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cards = input()
    hands = {'S':[],'C':[],'H':[],'D':[],}
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
    