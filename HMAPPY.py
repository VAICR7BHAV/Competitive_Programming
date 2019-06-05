import bisect
from sys import stdin,stdout
N,M=map(int,stdin.readline().split())
A=[int(i) for i in stdin.readline().split()]
B=[int(i) for i in stdin.readline().split()]

'''
for i in range(0,M):
    C[len(C)-1]=(C[len(C)-1][0]-C[len(C)-1][1],C[len(C)-1][1])
    C.sort()
print(max(C)[0])
'''
suma=sum(A)
i=0
if(M>=suma/2 and M<=suma):
    asfasf=3/0
less=suma-M
C=[]
cless=[]
for i in range(0,N):
    C.append((A[i] * B[i], B[i]))
    cless.append((B[i],A[i]))
#print('cless=',cless)
if(M<=less):
    #C = [(A[i] * B[i], B[i]) for i in range(0, len(A))]
    C.sort()
    while(M>0):
        if(M>=suma):
            break
        diff=C[N-1][0]-C[N-2][0]
        cneed=diff//C[N-1][1]+1
        if(cneed<=M):
            C[N-1]=(C[N-1][0]-C[N-1][1]*cneed,C[N-1][1])
            M-=cneed
            i+=cneed
        else:
            C[N-1]=(C[N-1][0]-C[N-1][1]*M,C[N-1][1])
            break
        last=C.pop()
        if(last[1]>C[N-3][0]):
            C.append(last)
            C[N-1],C[N-2]=C[N-2],C[N-1]
        else:
            pos=bisect.bisect_right(C,last)
            if(pos==len(C)):
                C.append(last)
            else:
                C.insert(pos,last)
        if(i>=suma):
            break
    stdout.write(str(max(C)[0]) + '\n')
else:
    cless.sort()
    ans=0
    while(less!=0):
        if(cless[0][1]>=less):
            ans+=cless[0][1]*less
            break
        else:
            ans+=cless[0][1]*cless[0][0]
            less-=cless[0][1]
            del cless[0]
    stdout.write(str(ans)+'\n')
