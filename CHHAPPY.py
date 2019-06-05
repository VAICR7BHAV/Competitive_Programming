from sys import stdin,stdout
from collections import Counter
import bisect
t=int(stdin.readline())
while(t>0):
    n=int(stdin.readline())
    A=[int(i) for i in stdin.readline().split()]
    ans=False
    B=[int(A[i]) for i in range(0,n)]
    B.sort()
    d=Counter(A)
    for key in d:
        if(d[key]>=2):
            ind=[(i+1) for i, e in enumerate(A) if e == key]
            l=len(ind)
            #print(ind)
            count=0
            for j in range(0,l):
                pos=bisect.bisect_right(B,ind[j])
                if(B[pos-1]==ind[j]):
                    count+=1
                if(count==2):
                    break
            if(count==2):
                ans=True
                break
        if(ans==True):
            break
    if(ans==True):
        stdout.write("Truly Happy"+'\n')
    else:
        stdout.write("Poor Chef"+'\n')
    t-=1