# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7 

# 1 2 7 3 6 5 
import sys
sys.stdin= open('input.txt')
V , Edge = map(int,input().split())
#인접리스트
M = [[]*V for _ in range(V)]
stack = []
#방문리스트
visited = [False]*V
for _ in range(Edge):
    f, t = map(int, input().split())
    M[f-1].append(t-1)

# stack.append(0)
# visited[0]= True
# A, B = M[0]
result = 1000

for i in range(len(M)):
    cnt = 0
    stack.append(i)
    visited[i]= True
    while stack:
        print(stack)
        for j in range(len(M[i])):
            if visited[M[i][j]]:
                continue
            elif not visited[M[i][j]]:                
                visited[M[i][j]] = True
                stack.append(M[i][j])
                cnt +=1
                i = stack[-1]
            elif not M[i]:
                stack.pop(i)
                i = stack[-1]
        if result > cnt:
            result = cnt
        if len(stack)==V and cnt<result:
            slist = stack
            # stack.pop(i)
print(slist, result)


        # if result > cnt:
        #     result = cnt

        



    
        
print('V',visited)
print('M',M)
print('S', stack)
