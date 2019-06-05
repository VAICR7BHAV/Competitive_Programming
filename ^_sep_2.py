n,w,b=map(int,input().split())
N=[int(i) for i in input().split()]
flag=1
exc=0
if(n%2==0):
    mid=n//2
    p1=N[0:mid]
    p2=N[mid:len(N)]
    #p1s=''
    #for i in range(0,len(p1)):
    #    p1s=p1s+str(p1[i])
    #p2s=''
    #p2.reverse()
    #for i in range(0,len(p2)):
    #   p2s=p2s+str(p2[i])
    #print(p1,p2)
    p2.reverse()
    wd=0
    bd=0

    for i in range(0,len(p1)):
        if(p1[i]!=p2[i]):
            if(p1[i]==2 and p2[i]==0):
                wd+=1
            elif(p1[i]==2 and p2[i]==1):
                bd+=1
            elif(p2[i]==2 and p1[i]==0):
                wd+=1
            elif(p2[i]==2 and p1[i]==1):
                bd+=1
            else:
                flag=0
                break
        elif (p1[i] == 2):
            exc += 2 * min(b, w)
else:
    mid = n // 2
    p1 = N[0:mid]
    p2 = N[mid+1:len(N)]
    p2.reverse()
    wd = 0
    bd = 0

    for i in range(0, len(p1)):
        if (p1[i] != p2[i]):
            if (p1[i] == 2 and p2[i] == 0):
                wd += 1
            elif (p1[i] == 2 and p2[i] == 1):
                bd += 1
            elif (p2[i] == 2 and p1[i] == 0):
                wd += 1
            elif (p2[i] == 2 and p1[i] == 1):
                bd += 1
            else:
                flag = 0
                break
        elif(p1[i]==2):
            exc+=2*min(b,w)
    if(N[mid]==2):
        exc+=min(w,b)
if(flag==0):
    print(-1)
elif(n!=1):
    print(wd*w+bd*b+exc)
elif(n==1 and N[0]==2):
    print(min(b,w))
else:
    print(0)