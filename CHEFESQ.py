from sys import stdin,stdout
N,Q=map(int,stdin.readline().split())
A=[int(i) for i in stdin.readline().split()]
def check(arr,k):
    xo=0
    for i in range(0,len(arr)):
        xo=xo^arr[i]
    if(xo==k):
        return True
    else:
        return False
def count(A,i,k):
    coun=0
    for j in range(1,i+1):
        #print(j)
        arr=(A[0:j])
        #print(arr)
        if(check(arr,k)):
            #print(arr)
            coun+=1
    #print('coun=',coun)
    return coun
for k in range(0,Q):
    q,i,k=map(int,stdin.readline().split())
    if(q==1):
        A[i-1]=k
    if(q==2):
        cou=0
        cou += count(A, i, k)
        stdout.write(str(cou)+'\n')