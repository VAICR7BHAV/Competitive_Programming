from sys import stdin,stdout
from itertools import combinations
from collections import Counter
t=int(stdin.readline())
#arr=[i for i in range(0,100001)]
while(t>0):
    n,k=map(int,stdin.readline().split())
    arra=[]
    ans=0
    for i in range(0,n):
        l,r=map(int,stdin.readline().split())
        arra.append((l,r))
    #print(arra)
    comb=(combinations(arra,k))
    for i in comb:
        tup1=i[0]
        tup2=i[1]
        arr1=[int(j) for j in range(tup1[0],tup1[1])]
        arr2=[int(j) for j in range(tup2[0],tup2[1])]
        #print(arr1,arr2)
        #arr1=arr[tup1[0]:tup1[1]]
        #arr2=arr[tup2[0]:tup2[1]]
        d1=Counter(arr1)
        d2=Counter(arr2)
        d3=d1&d2
        ans=max(ans,len(d3))
    stdout.write(str(ans)+'\n')
    t-=1
