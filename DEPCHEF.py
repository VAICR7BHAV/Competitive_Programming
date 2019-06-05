T=int(input())
while(T>0):
    N=int(input())
    A=[int(i) for i in input().split()]
    D=[int(i) for i in input().split()]
    ans=-1
    for i in range(N):
        left=i-1
        right=i+1
        if(i==0):
            left=N-1
        if(i==N-1):
            right=0
        if(D[i]>A[left]+A[right]):
            if(D[i]>=ans):
                ans=D[i]
    print(ans)
    T-=1