inp = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
a = [[] for _ in range((max(inp)+1))]
c = [False]*(max(inp)+1)
for i in range(0, len(inp), 2):
    a[inp[i]].append(inp[i+1])
res = ['1']
stk = [1]
while stk:
    for ai in a[stk[-1]]:
        if not c[ai]:
            c[ai] = True
            res.append(str(ai))
            stk.append(ai)
            break    
    stk.pop()
print('-'.join(res))