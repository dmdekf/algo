from collections import Counter
import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    d = list(input())
    c = Counter(d).most_common()
    max_num = c[0][1]
    max_cards = [x for x, y in c if y == max_num]
    print(f'#{tc} {max(max_cards)} {max_num}')
