def convert(col,row,direc,dis):
    p=dis
    if direc==2:
        p=2*col+row-dis
    if direc==3:
        p=2*(col+row)-dis
    if direc==4:
        p+=col
    return p
col, row=map(int, input().split())
N=int(input())
stores=[]
for _ in range(N):
    direc,dis= list(map(int,input().split()))
    p=convert(col,row,direc,dis)
    stores.append(p)
dong_dir, dong_dis=map(int,input().split())
dong=convert(col,row,dong_dir,dong_dis)
total=0
for i in range(N):
    a=abs(stores[i]-dong)
    b=2*(col+row)-a
    total+=min(a,b)
print(total)