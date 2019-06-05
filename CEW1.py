from bisect import bisect_left
import time

primen=[]
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
t1=time.time()
prime=SieveOfEratosthenes(1000000000000000001)
for i in range(2,len(prime)):
    if(prime[i]):
        primen.append(i)
primen[0]=1
#print(primen)
#print(primen2)
t2=time.time()
#print(t2-t1)
t=int(input())
for k in range(0,t):
    n=int(input())
    index=bisect_left(primen,n)
    if(n==2):
        print('1 2')
    elif(primen[index]==n):
        print(primen[index-1],primen[index])
    else:
        print(primen[index-2],primen[index-1])