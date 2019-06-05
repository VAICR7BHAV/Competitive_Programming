n=int(input())
p=[int(i) for i in input().split()]
minp=p[0]
maxp=p[0]
ans=0
for i in range(1,n):
    if(p[i]<minp):
        ans+=1
        minp=p[i]
    if(p[i]>maxp):
        ans+=1
        maxp=p[i]
print(ans)