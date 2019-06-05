import bisect
from sys import stdin,stdout
n=int(stdin.readline())
A=[int(i) for i in stdin.readline().split()]
ans=-1
if(A[0]!=0):
    ans=1
else:
    '''
    for i in range(0,n-1):
        if(A[i+1]>A[i]):
            if(A[i+1]-A[i]>1):
                ans=i+2
                break
    
    poss=[0]
    for i in range(0,n):
        num=A[i]
        pos=bisect.bisect_right(poss,num)
        #print(num,pos)
        if(poss[pos-1]==num):
            poss.append(A[i]+1)
        else:
            ans = i + 1
            break
    '''
    ma=A[0]
    for i in range(0,n-1):
        if(A[i+1]>ma):
            if(A[i+1]-ma==1):
                ans=-1
                ma=A[i+1]
            else:
                ans=i+2
                break
stdout.write(str(ans))