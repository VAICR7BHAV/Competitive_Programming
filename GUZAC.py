from sys import stdin,stdout
from collections import Counter
def S(n):
    ans=(n*(n+1))//2
    return ans
t=int(stdin.readline())
for g in range(0,t):
    n,k,x=map(int,stdin.readline().split())
    p=[int(i) for  i in stdin.readline().split()]
    p.sort()
    min=p[0]
    max=p[len(p)-1]
    suma = sum(p)
    p.append(min+x+1)
    count=0
    v=Counter(p)
    #print(p)
    total=n-k
    for i in range(len(p)-1,0,-1):
        n1=p[i]-1
        n2=p[i-1]
        if(total==0):
            break
        if(total>=n1-n2):
            suma+=S(n1)-S(n2)
            total-=n1-n2
        else:
            ex=n1-n2-total
            suma+=S(n1)-S(n2+ex)
            total=0
    stdout.write(str(suma)+'\n')