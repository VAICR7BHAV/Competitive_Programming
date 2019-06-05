from collections import Counter
T=int(input())
while(T>0):
    N=int(input())
    s=input()
    d1=Counter(s)
    for i in range(N-1):
        S=input()
        d2=Counter(S)
        d1=d1&d2
    print(len(d1))
    T-=1