from sys import stdin,stdout
t=int(stdin.readline())
while(t>0):
    n,k=map(int,stdin.readline().split())
    A=[int(i) for i in stdin.readline().split()]
    s=''
    for i in range(0,n):
        if(k>=A[i]):
            k-=A[i]
            s=s+'1'
        else:
            s=s+'0'
    stdout.write(s+'\n')
    t-=1