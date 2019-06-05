from sys import stdin,stdout
import bisect
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
prime=SieveOfEratosthenes(200)
primen=[]
for i in range(0,200):
    if(prime[i]):
        primen.append(i)
semiprime=[]
for i in range(0,len(primen)):
    for j in range(i+1,len(primen)):
        semiprime.append(primen[i]*primen[j])
sop=[]
for i in range(0,len(semiprime)):
    for j in range(i,len(semiprime)):
        sop.append(semiprime[i]+semiprime[j])
sop.sort()
t=int(stdin.readline())
while(t>0):
    n=int(stdin.readline())
    ans=""
    pos=bisect.bisect_right(sop,n)
    if(sop[pos-1]==n):
        ans="YES"
    else:
        ans="NO"
    stdout.write(ans+'\n')
    t-=1