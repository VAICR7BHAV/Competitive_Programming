n,k=map(int,input().split())
limit=[0]*502
count=0
j=2
i=2
while(i!=500):
        for h in range(j+1):
            limit[i]=j
            i+=1
            if(i==500):
                break
        j+=1
if(k<=limit[n]):

    x=[]
    if(k==1):
        x.append(n)
        print("here")
    elif(k==2):
        if(n%2==0):
            x.append(n//2+1)
            x.append(n//2-1)
        else:
            x.append(n//2)
            x.append(n//2+1)
    elif(k==3):
        rem=n%k
        quo=n//k
        if(rem==1 or rem==0):
            x.append(n//3+1+rem)
            x.append(n//3-1)
            x.append(n//3)
        else:
            x.append(n // 3 + 1)
            x.append(n // 3 - 1)
            x.append(n // 3+rem)
    elif(k==4):
        quo=n//k
        rem=n%k
        if(rem==3 or rem==2):
            x.append(quo+1)
            x.append(quo-1)
            x.append(quo+rem)
            x.append(quo)
        elif(rem==0):
            x.append(quo + 1)
            x.append(quo - 1)
            x.append(quo-2)
            x.append(quo+2)
        else:
            x.append(quo+2*rem)
            x.append(quo+1*rem)
            x.append(quo)
            x.append(quo-2*rem)
    print(x)