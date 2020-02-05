
# 3
# S01D02H03H04
# H02H10S11H02
# S10D10H10C01  

# #1 12 12 11 13
# #2 ERROR
# #3 12 12 12 12 	// Test Case 1의 정답
# // Test Case 2의 정답
# // Test Case 3의 정답
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
        else:
            for i in d[::3]:
                if i == 'S':
                    S -=1
                if i == 'D':
                    D -=1
                if i == 'H':
                    H -=1
                if i == 'C':
                    C -=1
            result = '{} {} {} {}'.format(S, D, H, C)
            break    

    print('#{} {}'.format(tc, result))
