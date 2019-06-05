t=int(input())
while(t>0):
    n,k=map(int,input().split())
    A=[int(i) for i in input().split()]
    B=[int(i) for i in input().split()]
    ans=0
    for i in range(0,n):
        stones=k//A[i]
        profit=stones*B[i]
        if(profit>=ans):
            ans=profit
    print(ans)
    t-=1