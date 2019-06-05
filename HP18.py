t=int(input())
while(t>0):
    N,a,b=map(int,input().split())
    A=[int(i) for i in input().split()]
    A.sort()
    Alice=[]
    Bob=[]
    for i in range(0,N):
        if(A[i]%a==0):
            Bob.append(A[i])
        elif(A[i]%b==0):
            Alice.append(A[i])
    if(len(Bob)>len(Alice)):
        print("BOB")
    else:
        print("ALICE")
    t-=1