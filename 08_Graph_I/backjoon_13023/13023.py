import sys
sys.stdin = open('input.txt')

# def c(d):
#     for i in range(len(d)):
#         for d[d[i]]:

V, Edge = map(int,input().split())
M = [[0]*V for _ in range(V)]
#{node :[e1,e2]}
# G = {i : [] for i in range(V)}
G = [[] for _ in range(V)]
F = []
for _ in range(Edge):
    f, t = map(int, input().split())
    #인접행렬
    #[[]]
    M[f][t] = M[t][f] = 1

    #인접 리스트
    #{f :[t1,t2]}
    G[f].append(t)
    G[t].append(f)

    #edge
    F.append([f, t])
    F.append([t, f])
#각각의 노드를 검사
for i in range(len(F)):
    for j in range(len(F)):
        A, B = F[i]
        C, D = F[j]
        #만들지 못하는 것들을 필터링
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not M[B][C]:
            continue
        for E in G[D]:
            if E == A or E == B or E == C or E == D:
                continue
            print(1)
            sys.exit(0)

print(0)

print('G',G)
print('M',M)
print('F',F)

