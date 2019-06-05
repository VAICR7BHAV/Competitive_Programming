from collections import Counter
n=int(input())
s=input()
ans="YES"
stri=""
'''
for i in range(0,n):
    for j in range(i,n):
        st=(s[i:j+1])
        d=Counter(st)
        #print(d)
        for k in d:
            #print(d[k],len(st)/2)
            if(d[k]>len(st)/2):
                ans="NO"
                break
            else:
                ans="YES"
        #print(ans)
        if(ans=="YES"):
            stri=st
            break
    if(ans=="YES"):
        break
'''
st=""
d=Counter(s)
for k in d:
    d[k]=0
for i in range(0,n):
    st=s[i]
    d[s[i]]+=1
    for j in range(i+1,n):
        st=st+s[j]
        d[s[j]]+=1
        for k in d:
            if(d[k]>len(st)/2):
                ans="NO"
            else:
                ans="YES"
                stri=st
                break
    if(ans=="YES"):
        break
if(ans=="YES"):
    print(ans)
    print(stri)
else:
    print(ans)