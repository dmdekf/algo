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
M = [[] for _ in range(V+1)]
stack = []
#방문리스트
visited = [False for _ in range(V+1)]
for _ in range(Edge):
    f, t = map(int, input().split())
    M[f].append(t)
print('M',M)
print('V',visited)
cnt = 0
stack.append(i)
visited[i]= True
while stack:
    print(stack)
    for j in M[i]:
        if visited[j]:
            continue
        elif not visited[j]:                
            visited[j] = True
            stack.append(j)
            cnt +=1
            
        elif not M[i]:
            stack.pop(i)
            i = stack[-1]
        # if result > cnt:
        #     result = cnt
        # if len(stack)==V and cnt<result:
        #     slist = stack
        #     # stack.pop(i)
        
print('V',visited)
print('M',M)
print('S', stack)
