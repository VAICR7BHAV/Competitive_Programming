from sys import stdin,stdout
t=int(stdin.readline())
while(t>0):
    n,m,x,y=map(int,stdin.readline().split())
    n-=1
    m-=1
    nr=n%x
    pr=m%y
    ans='Pofik'
    if(n==1 and m==1):
        ans='Chefirnemo'
    elif((nr==0 and pr==0) or (nr==1 and pr==1)):
        ans='Chefirnemo'
    else:
        ans='Pofik'
    stdout.write(ans+'\n')
    t-=1