t=int(input())
while(t>0):
    ns=[i for i in input().split()]
    n=int(ns[0])
    s=ns[1]
    B=[]
    le=[]
    for i in range(0,n):
        st=input()
        B.append(st)
        le.append(len(st))
    if(s=="Dee"):
        ans=0
        for i in range(0,n):
            if(B[i][0]=='0'):
                ans=ans^le[i]
        if(ans!=0):
            print("Dee")
        else:
            print("Dum")
    else:
        ans=0
        for i in range(0,n):
            if(B[i][0]=='1'):
                ans=ans^le[i]
            if (ans != 0):
                print("Dee")
            else:
                print("Dum")
    t-=1