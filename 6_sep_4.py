import bisect
n,k=map(int,input().split())
N=[int(i) for i in input().split()]
N2=[]
N.sort()
ans=-1
for i in range(0,n-1):
    if(N[i]==N[i+1]):
        ans=0
        break
if(ans!=0):
    for i in range(0,n):
        N2.append(N[i])
    for i in range(0,n):
        N2[i]=N2[i]&k
        pos=bisect.bisect_right(N,N2[i],0,n)
        if(pos>0 and N[pos-1]==N2[i] and pos-1!=i):
            ans=1
            break
        else:
            ans=-1
print(ans)