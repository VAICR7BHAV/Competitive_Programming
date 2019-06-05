def f(n):
    count=1
    while(n!=1):
        print(n,end=' ')
        count+=1
        if(n%2!=0):
            n=3*n+1
        else:
            n=n//2
    print(1)
    print(count)
for i in range(1,11):
    f(i)