import sys

sys.stdin = open('input.txt')


T = 10
for _ in range(T):
    tx = int(input())
    d = [list(map(int,input().split())) for _ in range(100)]
    for i in range(100):
        d[i].append(0)
        d[i].insert(0,0)
    result = 1000
    cnt = 1000000
    # 각 사다리 점검하기.
    for i in range(100,-1,-1):
        c = i
        r = 0
        temp = 0
        if d[r][c]:
            while r !=100:
                if c < 101 and d[r][c+1]:                            while d[r][c]:
                        temp +=1
                        c +=1
                    r = r+1
                    temp +=1 
                elif c > 0 and d[r][c-1]:       
                    while d[r][c]:
                        temp +=1
                        c -=1
                    r = r+1
                    temp +=1 
                elif d[r+1][c]:
                    r = r+1
                    temp +=1 
            # print(temp, i)
            if cnt > temp :
                cnt = temp
                result = i
            
        
    print(result-1, cnt)
    




        
                