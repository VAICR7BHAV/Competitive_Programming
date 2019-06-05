import bisect
n,q=map(int,input().split())
A=[int(i) for i in input().split()]
B=[]
for i in range(0,n):
    B.append(A[i])
A.sort()
B.sort()
#print(A)
for i in range(0,q):
    for j in range(0,n):
        A[j]=B[j]
    v=int(input())
    ans=0
    count=0
    cond=True
    while(True):
        pos=bisect.bisect_left(A,v,0,n)
        #print(pos)
        count+=1
        if(count>n):
            ans=-1
            break
        #print(pos)
        if(pos==0):
            if(v!=0):
                cond=False
            if(v==A[0]):
                ans=ans+1
                cond=True
                v=v-A[0]
                A[0]=0
                A.sort()
            if(v==0):
                cond=True
                break
            else:
                break
        else:
            if (pos >= n):
                pos = pos - 1
            if(A[pos]>v):
                pos=pos-1
            val=A[pos]
            v=v-val
            A[pos]=0
            A.sort()
            ans=ans+1
    if(cond):
        if(ans!=-1):
            print(ans-1)
        else:
            print(ans)
    else:
        print(-1)