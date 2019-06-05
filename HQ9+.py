from collections import Counter
p=input()
d=Counter(p)
if(d['H']>=1 or d['Q']>=1 or d['9']>=1):
    print("YES")
else:
    print("NO")