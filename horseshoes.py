from collections import Counter
s=[int(i) for i in input().split()]
d=Counter(s)
ans=0
for key in d:
    if(d[key]!=1):
        if(d[key]==2):
            ans+=1
        if(d[key]==3):
            ans+=2
        if(d[key]==4):
            ans+=3
print(ans)