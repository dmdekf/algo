import sys

sys.stdin = open('s_input.txt')

def c(x):
    n = [[0]*len(x) for _ in range(len(x))]
    
    for i in range(len(x)):
        for j in range(len(x)):
            n[j][len(x)-1-i] =  x[i][j]                              
    return n
    
T = int(input())
for tc in range(1, T +1):
    N, key = map(str,input().split())
    N = int(N)
    d = [(list(map(int,input().split()))) for _ in range(N)]
    if key =='up':
        d = c(d)
            
    if key == 'down':
        d = c(c(c(d)))
      
    if key == 'left':
        d = c(c(d))  

    for i in range(N):
        for j in range(N-1,-1,-1):
            chk = 0
            # if key == 'left':
            if j != N-1 and d[i][j]:
                while j != N-1 and d[i][j+1] ==0:
                    d[i][j+1] = d[i][j] 
                    d[i][j] = 0
                    j +=1
                if j != N-1 and d[i][j] == d[i][j+1]:
                    d[i][j+1] = str(d[i][j]+d[i][j+1])
                    d[i][j] = 0
    if key =='left':
        d = c(c(d))
            
    if key == 'down':
        d = c(d)
      
    if key == 'up':
        d = c(c(c(d)))

    print('#{}'.format(tc))
    for i in range(N):
        print(*d[i],end='')
        print()
        

  


    

                        
                    
                    