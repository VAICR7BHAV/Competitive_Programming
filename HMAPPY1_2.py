from sys import stdin,stdout
from collections import Counter
def q1(A):
    l=len(A)
    B=[A[l-1]]*l
    for i in range(0,l-1):
        B[i+1]=A[i]
    return B
def q2(s):
    max=0
    l=len(s)
    for i in range(0,l-1):
        count=1
        if(s[i]==1):
            for j in range(i+1,l):
                if(s[j]==1):
                    count+=1
                else:
                    break
            if(count>max):
                max=count
    return max
N,Q,K=map(int,stdin.readline().split())
A=[int(i) for i in stdin.readline().split()]
ans=[]
flag=True
max=q2(A)
count=0
ar=[]
bcond=False
i=0
lcount=0
dicti=Counter(A)
visited=[False]*N
rend=N-1
lend=0
if(dicti[0]==N):
    ar.append(0)
if(dicti[1]==N):
    ar.append(N)
elif(A[0]==1 and A[N-1]==1):
    count=0
    for i in range(0,N):
        if(A[i]==1):
            visited[i]=True
            count+=1
        else:
            lend=i
            break
    for i in range(N-1,0,-1):
        if(A[i]==1):
            visited[i]=True
            count+=1
        else:
            rend=i
            break
if(count!=0):
    ar.append(count)
    count=0
for i in range(lend,rend+1):
    if(visited[i]==False):
        if(A[i]==1):
            count+=1
        elif(count>0):
            ar.append(count)
            count=0
'''
while(True):
    if(dicti[1]==N):
        ar.append(N)
        break
    if(A[i]==1):
        count+=1
    elif(count>0):
        ar.append(count)
        count=0
        if(bcond):
            break
    if(i==N-1):
        if(A[N-1]==1):
            i=-1
            bcond=True
        else:
            break
    i+=1
'''
#print(ar)
ar.sort()
d=Counter(ar)
#print(d)
minimum=0
lenar=len(ar)
element=ar[lenar-1]
if(dicti[1]==N):
    minimum=N
elif(d[element]>1):
    minimum=element
else:
    mid=0
    if(element%2==0):
        mid=element//2
    else:
        mid=element//2+1
    if(lenar>1):
        minimum=max(mid,ar[lenar-2])
    else:
        minimum=mid
#print(minimum)
if(dicti[1]==N):
    if(N<=K):
        ans=[N]*N
    else:
        ans=[K]*N
elif(dicti[0]==N):
    ans=[0]*N
elif(d[element]>1):
    if(element<=K):
        ans=[element]*N
    else:
        ans=[K]*N
else:
    if(lenar==1):
        curr=q2(A)
        ans.append(curr)
        while(curr!=element):
            curr+=1
            ans.append(curr)
        for j in range(0,dicti[0]):
            ans.append(element)

        while(curr!=minimum):
            curr-=1
            ans.append(curr)
            if (len(ans) == N):
                break
        if (element % 2 != 0):
            ans.append(minimum)
        while(len(ans)!=N):
            if (len(ans) == N):
                break
            if(curr<element):
                while(curr!=element):
                    curr+=1
                    ans.append(curr)
                    if(len(ans)==N):
                        break
            else:
                while(curr!=minimum):
                    curr-=1
                    ans.append(curr)
                    if (len(ans) == N):
                        break
            if (len(ans) == N):
                break
        #print(ans)
    else:
        for i in range(0,N):
            if(flag):
                ans.append(max)
            else:
                aasdf=q2(A)
                ans.append(aasdf)
                max=aasdf
            if(A[N-1]==0):
                flag=True
            else:
                flag=False
            A=q1(A)
print(ans)
q=stdin.readline()
count=0
for i in range(0,Q):
    if(q[i]=='!'):
        count+=1
        if(count>=N):
            count=count%N
    else:
        try:
            if(ans[count]<=K):
                stdout.write(str(ans[count])+'\n')
            else:
                stdout.write(str(K)+'\n')
        except:
            stdout.write(str(K) + '\n')