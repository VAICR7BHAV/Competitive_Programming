from sys import stdin,stdout
from collections import Counter
def q1(A):
    l=len(A)
    B=[A[l-1]]*l
    for i in range(0,l-1):
        B[i+1]=A[i]
    return B
def q2(A,K):
    currm=0
    count=0
    for i in range(0,len(A)):
        if(A[i]==1):
            count+=1
        else:
            currm=max(currm,count)
            count=0
        if(currm>=K):
            return K
    return max(currm,count)
N,Q,K=map(int,stdin.readline().split())
A=[int(i) for i in stdin.readline().split()]
flag=True
ini=q2(A,K)
ans=[ini]*N
q=stdin.readline()
count=0
dicti=Counter(q)
#print(dicti)
count1=dicti['!']
for i in range(0,count1):
    A = q1(A)
    ans[i+1]=q2(A,K)
for i in range(0,Q):
    if(q[i]=='!'):
        count+=1
        if(count>=N):
            count=count%N
    else:
        stdout.write(str(ans[count])+'\n')
'''
for i in range(0,Q):
    if(q[i]=='!'):
        A=q1(A)
        flag=False
    if(q[i]=='?'):
        if(flag):
            stdout.write(str(ans)+'\n')
        else:
            ans=q2(A,K)
            stdout.write(str(ans)+'\n')
        flag=True
'''