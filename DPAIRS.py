N,M=map(int,input().split())
A=[int(i) for i in input().split()]
B=[int(i) for i in input().split()]
A.sort()
B.sort()
count=0
for i in range(0,N):
    for j in range(i,M):
        print(i,j)
        count+=1
        if(count==N+M-1):
            break