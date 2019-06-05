n,d=map(int,input().split())
A=[int(i) for i in input().split()]
count=0
A.sort()
for i in range(A[0],A[len(A)-1]):
    dis=[]
    for j in range(0,n):
        dis.append(abs(A[j]-i))
    dis.sort()
    if(dis[0]==d):
        count+=1
print(count+2)