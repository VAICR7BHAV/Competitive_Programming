def ideal(M1,M2,N,M):
    s1=''
    s2=''
    for i in range(0,M):
        if(i%2==0):
            s1=s1+'R'
            s2=s2+'G'
        else:
            s1=s1+'G'
            s2=s2+'R'
    for i in range(0,N):
        if(i%2==0):
            M1.append(s1)
            M2.append(s2)
        else:
            M1.append(s2)
            M2.append(s1)
t=int(input())
for k in range(0,t):
    N,M=map(int,input().split())
    inp=[]
    M1=[]
    M2=[]
    ideal(M1,M2,N,M)
    C1R=0
    C1G=0
    C2R=0
    C2G=0
    for i in range(0,N):
        s=M1[i]
        s2=M2[i]
        s1=input()
        for j in range(0,len(s)):
            if(s[j]=='R' and s1[j]=='G'):
                C1R+=1
            if(s[j]=='G' and s1[j]=='R'):
                C1G+=1
            if(s2[j]=='G' and s1[j]=='R'):
                C2G+=1
            if(s2[j]=='R' and s1[j]=='G'):
                C2R+=1
    cost1=C1R*3+C1G*5
    cost2=C2R*3+C2G*5
    print(min(cost1,cost2))

