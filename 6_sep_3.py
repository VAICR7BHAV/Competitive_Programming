from sys import stdin,stdout
n=int(stdin.readline())
A=[int(i) for i in stdin.readline().split()]
ans=[1]*n
check=[False]*n
for i in range(0,n):
    if(check[i]==False):
        for j in range(i,n-1):
            if(2*A[j]>=A[j+1]):
                ans[i]+=1
                check[j]=True
            else:
                i=j+1
                break
ans.sort()
'''
while(pos!=n or pos!=n-1):
    for i in range(pos,n-1):
        if(2*A[i]>=A[i+1]):
            ans[i]+=1
        else:
            pos=i
            break
'''
print(ans[len(ans)-1])