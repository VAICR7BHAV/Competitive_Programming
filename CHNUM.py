t=int(input())
while(t>0):
    N=int(input())
    A=[int(i) for i in input().split()]
    A.sort()
    co=0
    ce=0
    for i in range(0,N):
        if(A[i]<0):
            co+=1
        else:
            ce+=1
    if(co>ce and ce!=0):
        print(co,ce)
    elif(ce>co and co!=0):
        print(ce,co)
    elif(ce==0):
        print(co,co)
    elif(co==0):
        print(ce,ce)
    t-=1