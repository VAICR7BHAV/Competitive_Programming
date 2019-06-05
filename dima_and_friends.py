n=int(input())
a=[int(i) for i in input().split()]
suma=sum(a)
ans=0
for i in range(1,6):
    if((suma+i)%(n+1)!=1):
        ans+=1
print(ans)