t=int(input())
for q in range(0,t):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=sorted(a)
    if b==a:
        print("YES")
    else:
        for i in range(1,n):
            if a[i]<a[i-1]:
                break
        b=a[0:i]
        c=a[i:n]
        #print(b,c)
        d=[c[i] for i in range(0,len(c))]
        e=[b[i] for i in range(0,len(b))]
        f=d+e
        #print(f,a)
        if f==(sorted(a)):
            print("YES")
        else:
            print("NO")