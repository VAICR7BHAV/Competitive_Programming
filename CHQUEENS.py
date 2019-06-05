from sys import stdin,stdout
t=int(stdin.readline())
while(t>0):
    n,m,X,Y=map(int,stdin.readline().split())
    ansf=0
    for x in range(1,n+1):
        for y in range(1,m+1):
            ans=0
            if(X==x):
                ans+=n+m-X
            elif(Y==y):
                ans+=m+n-Y
            else:
                ans+=n+m-1
            if(True):
                i=x
                j=y
                count=0
                while(True):
                    if(i+1<=n and j-1>=1 and (i+1!=X and j-1!=Y)):
                        count+=1
                        i+=1
                        j-=1
                    else:
                        break
                i=x
                j=y
                while(True):
                    if(i-1>0 and j-1>0 and(i-1!=X and j-1!=Y)):
                        count+=1
                        i-=1
                        j-=1
                    else:
                        break
                i=x
                j=y
                while(True):
                    if(i-1>=0 and j+1<=m and (i-1!=X and j+1!=Y)):
                        count+=1
                        i-=1
                        j+=1
                    else:
                        break
                while(True):
                    if(i+1<=n and j+1<=m and (i+1!=X and j+1!=Y)):
                        count+=1
                        i+=1
                        j+=1
                    else:
                        break
                ans+=count
            if(X==x and Y==y):
                ans=0
            print(x,y,ans)
        ansf+=n*m-ans
    print(ansf)
    t-=1