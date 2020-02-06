import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{} '.format(tc))
    N = int(input())
    
    prev_line = [0,1,0]
    print(''.join(str(n) for n in prev_line[1:-1]))
    for lenght in range(2, N+1):
        curr_line = [0] + [prev_line[i] + prev_line[i+1] for i in range(lenght)]+ [0] 
        print(' '.join([str(n) for n in curr_line[1:-1]]))
        prev_line = curr_line   


