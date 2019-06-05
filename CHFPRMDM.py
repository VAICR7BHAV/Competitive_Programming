from sys import stdin,stdout
from collections import Counter
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p+=1
    prime[0]=False
    prime[1]=False
    return prime
prime=SieveOfEratosthenes(1000000)
t=int(stdin.readline())
while(t>0):
    n=int(stdin.readline())
    arr=[int(i) for i in stdin.readline().split()]
    for i in range(0,len(arr)):
        if(prime[arr[i]]):
            arr[i]=1
        else:
            arr[i]=0
    flag=0
    ans=1
    for i in range(0,n+1):
        for j in range(i+1,n+1):
            if(j-i>ans):
                a=(arr[i:j])
                d1=Counter(a)
                if(d1[1]>d1[0]):
                    if(len(a)>ans):
                        ans=len(a)
                        flag=1
    print(ans)
    t-=1