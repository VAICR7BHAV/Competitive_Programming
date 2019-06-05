from sys import stdin,stdout
def q1(A):
    l=len(A)
    B=[A[l-1]]*l
    for i in range(0,l-1):
        B[i+1]=A[i]
    return B
'''
def q1(a):
    l=len(a)
    b=a[0:l-1]
    if (a[l - 1] == '0'):
        b='0'+b
    else:
        b='1'+b
    return b

def q2(X,Y,m,n,K):
    LCSuff = [[0 for k in range(n + 1)] for l in range(m + 1)]
    result = 0
    flag=False
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                result = max(result, LCSuff[i][j])
                if(result==K):
                    flag=True
                    break
            else:
                LCSuff[i][j] = 0
        if(flag):
            break
    return result
'''
def q2(s,K):
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
        if(max>=K):
            max=K
            break
    return max
N,Q,K=map(int,stdin.readline().split())
A=[int(i) for i in stdin.readline().split()]
'''
ms=''
check=''
for i in range(0,N):
    ms+=str(A[i])
    check+='1'
'''
maxa=q2(A,K)
flag=True
ini=0
if(A[0]==0):
    ini=0
else:
    for i in range(1,N):
        if(A[i]==1):
            ini+=1
        if(ini==K):
            break
        else:
            break
end=0
if(A[N-1]==0):
    end=0
else:
    for i in range(N-1,0,-1):
        if(A[i]==1):
            end+=1
        if(end==K):
            break
        else:
            break
q=stdin.readline()
for i in range(0,Q):
    if(q[i]=='!'):
        if(A[N-1]==0):
            flag=True
        else:
            flag=False
        A=q1(A)
    elif(q[i]=='?'):
        an=0
        if(flag):
            an=maxa
        else:
            ini+=1
            end-=1
            if(ini==K):
                an=ini
            elif(end==K):
                an=end
            else:
                an=q2(A,K)
                maxa=an
        stdout.write(str(an)+'\n')