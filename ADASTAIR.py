from sys import stdin,stdout
t=int(stdin.readline())
while(t>0):
    n,k=map(int,stdin.readline().split())
    h=[int(i) for i in stdin.readline().split()]
    count=0
    d=[]
    d.append(h[0])
    for i in range(1,len(h)):
        d.append(h[i]-h[i-1])
    #print(d)
    for i in range(0,len(d)):
        if(d[i]>k):
            add=d[i]//k
            if(k*add==d[i]):
                count+=add-1
            else:
                count+=add
    stdout.write(str(count)+'\n')
    t-=1