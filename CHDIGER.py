t=int(input())
while(t>0):
    N,d=map(int,input().split())
    NS=str(N)
    temp=NS
    for i in range(0,len(NS)):
        temp=NS+str(d)
        for j in range(0,len(NS)):
            temp2=(temp[0:j]+temp[j+1:])
            if(int(temp2)<int(NS)):
                NS=temp2
    print(NS)
    t-=1