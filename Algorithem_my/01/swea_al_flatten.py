for tc in range(1,11):
    try_num=int(input())
    case_num=list(map(int,input().split()))
    num_num=[0]*101
    cnt = 0
    minnum =0
    maxnum = 0
    
    for c in case_num:
        num_num[c] +=1

    for _ in range(try_num):
        
        maxcnt = True
        mincnt = True
        for idx,i in enumerate(num_num):
            if i and mincnt :
                num_num[idx] -=1
                num_num[idx+1] +=1
                if num_num[idx]:
                    minnum = idx
                else:
                    minnum =idx+1
                mincnt =False
            if num_num[-idx] and maxcnt :
                num_num[-idx] -=1
                num_num[-idx-1] +=1
                if num_num[-idx]:
                    maxnum = -idx+100
                else:
                    maxnum = -idx+99
                maxcnt = False
            if not (maxcnt and mincnt):
                break
    print(cnt,maxnum,minnum)
    cnt = maxnum - minnum

    print('#{} {}'.format(tc,cnt))