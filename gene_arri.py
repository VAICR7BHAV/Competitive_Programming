n=int(input())
a=[int(i) for i in input().split()]
maxp=0
minp=0
max=a[0]
min=a[0]
for i in range(0,n):
    if(a[i]>max):
        max=a[i]
        maxp=i
    if(a[i]<=min):
        min=a[i]
        minp=i
if(maxp>minp):
    ans=maxp+n-2-minp
else:
    ans=maxp+n-1-minp
print(ans)