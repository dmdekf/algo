from collections import Counter
import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    d = list(input())
    c = Counter(d).most_common() # 빈도수, 가장 큰 값부터 정렬하여 list('value', count) return 
    max_num = c[0][1]
    max_cards = [x for x, y in c if y == max_num]
    print(f'#{tc} {max(max_cards)} {max_num}')
