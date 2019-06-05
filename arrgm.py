import collections
import math

t=int(input())
for q in range(0,t):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    d=collections.Counter(b)
    flag=0
    c=[]
    g=0
    count=0
    for i in range(0,n):
        if d[a[i]]>=0:
            c.append(a[i])
            l=collections.Counter(c)
            g=a[i]
            for j in range(0,n):
                if l[a[j]]==0:
                    m=math.gcd(a[i],a[j])
                    if m==1:
                        count+=1
            #print(count)
            if count>=(n-1):
                g=1
                break
    #print(count)
    if g==1:
        print("0")
        print(*a,sep=" ")
    else:
        print("1")
        a[0]=47
        print(*a,sep=" ")