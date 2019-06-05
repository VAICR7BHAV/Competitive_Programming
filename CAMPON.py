T=int(input())
while(T>0):
    D=int(input())
    arr=[0]*31
    for i in range(0,D):
        di,pi=map(int,input().split())
        arr[di-1]=pi
    prob=[0]*31
    curr=0
    for i in range(0,31):
        curr=curr+arr[i]
        prob[i]=curr
    #print(prob)
    Q=int(input())
    for i in range(0,Q):
        deadi,reqi=map(int,input().split())
        if(reqi>prob[deadi-1]):
            print("Go Sleep")
        else:
            print("Go Camp")
    T-=1