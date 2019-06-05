from sys import stdin,stdout
t,k=map(int,stdin.readline().split())
A=[1]*100001
ans=[]
sum=1
for i in range(0,100001):
    if(i<k):
        A[i]=1
    elif(i==k):
        A[i]=2
    else:
        A[i]=(A[i-1]%1000000007+A[i-k]%1000000007)%1000000007
    sum=(sum%1000000007+A[i]%1000000007)%1000000007
    ans.append(sum)
for i in range(0,t):
    a,b=map(int,stdin.readline().split())
    an=ans[b]-ans[a-1]
    an=an%1000000007
    stdout.write(str(an)+'\n')`