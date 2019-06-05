t=int(input())
while(t>0):
    s=[i for i in input().split()]
    ind=0
    for i in range(0,len(s)):
        if(s[i]==("not")):
            ind=1
            break
        else:
            ind=-1
    if(ind==-1):
        print("regularly fancy")
    else:
        print("Real Fancy")
    t=t-1