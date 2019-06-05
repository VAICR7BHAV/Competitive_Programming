from sys import stdout,stdin
t=int(stdin.readline())
while(t>0):
    n,m=map(int,stdin.readline().split())
    A=[int(i) for i in stdin.readline().split()]
    B=[int(i) for i in stdin.readline().split()]
    ans="Alice"
    A.sort()
    B.sort()
    if(A==B):
        ans="Bob"
    stdout.write(ans+'\n')
    t-=1