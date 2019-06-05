from sys import stdin,stdout
import bisect
t=int(stdin.readline())
while(t>0):
    n,m=map(int,stdin.readline().split())
    inte=[]
    for i in range(0,n):
        L, R = map(int, stdin.readline().split())
        a=(L,R)
        inte.append(a)
    inte.sort()
    #print(inte)
    #print(inte[0][0])
    for i in range(0,m):
        num=int(stdin.readline())
        y=(num,0)
        pos=bisect.bisect_right(inte,y)
        #print(pos)
        ans=0
        if(pos>len(inte)):
            ans=-1
        elif (num >= inte[pos - 1][0] and num < inte[pos - 1][1]):
            ans = 0
        elif(pos>=len(inte)):
            ans=-1
        elif(num>=inte[pos][0] and num<inte[pos][1]):
            ans=0
        elif(pos<len(inte)):
            ans=inte[pos][0]-num
        else:
            ans=-1
        print(ans)
    t-=1