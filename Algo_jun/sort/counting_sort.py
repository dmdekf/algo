A = [0,4,1,3,1,2,4,1]
N = len(A)
K = 4 #최대값

b = [0] * N
c = [0] *(K+1)
#ver1
for i in A:
    C[i] +=1

for i in range(1,K+1):
    c[i] +=c[i-1]

for i in A:
    c[i] -=1
    b[c[i]] = i

#ver2
b = []
for i in A:
    c[i] +=1

for i in range(K+1):
    b +=c[i]*[i]

