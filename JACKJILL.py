from sys import stdin,stdout
t=int(stdin.readline())
while(t>0):
    N,K,d=map(int,stdin.readline().split())
    jack=[int(i) for i in stdin.readline().split()]
    jill=[int(i) for i in stdin.readline().split()]
    sum=0
    flag=1
    for i in range(0,K):
        sum+=jack[i]+jill[i]
        if(sum>=d):
            flag=0
            break
    count=0
    if(flag==1):
        for i in range(K,N):
            sum=sum-jack[count]-jill[count]+jack[i]+jill[i]
            count+=1
            if(sum>=d):
                flag=0
                break
    if(flag==0):
        stdout.write("no\n")
    else:
        stdout.write("yes\n")
    t-=1
