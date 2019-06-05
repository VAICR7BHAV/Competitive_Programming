from sys import stdin, stdout
import math

m = 1000000007
t = int(input())
for i in range(0, t):
    a, b, n = map(int, input().split())
    # num = a ** n + b ** n
    diff = abs(a - b)
    g=-1
    if(a==b):
        g=(pow(a,n,1000000007)+pow(b,n,1000000007))%1000000007
    else:
        val1=pow(a,n,diff)
        val2=pow(b,n,diff)
        val=val1+val2
        g=math.gcd(val,diff)
    if(g<0):
        g=1
    print(g%1000000007)