from collections import Counter
t=int(input())
while(t>0):
    n,k=map(int,input().split())
    A=[int(i) for i in input().split()]
    d=Counter(A)
    ini=d[1]
    if(ini+k>=n):
        print("YES")
    else:
        print("NO")
    t-=1