n,m=map(int,input().split())
c=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
count=0
for i in range(0,n):
    #print(i)
    if(a[0]>=c[i]):
        #print(a[0],c[i])
        del(a[0])
        count+=1
    if(len(a)==0):
        break
print(count)