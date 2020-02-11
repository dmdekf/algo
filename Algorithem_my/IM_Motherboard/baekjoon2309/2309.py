import sys
sys.stdin = open('input.txt')
d = []
for _ in range(9):
    d.append(int(input()))
tempd = sum(d)
chak= False
for i in d:
    for j in d:
        if i!=j and tempd -(i+j) ==100 :
            d.remove(i)
            d.remove(j)
            chak = True
            break
    if chak == True:
        break
d=sorted(d)
# print(sum(d))

for i in range(len(d)):
    print(d[i])






