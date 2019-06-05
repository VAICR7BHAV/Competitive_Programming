n=int(input())
lo=0
ro=0
lc=0
rc=0
for i in range(0,n):
    li,ri=map(int,input().split())
    if(li==1):
        lo+=1
    else:
        lc+=1
    if(ri==1):
        ro+=1
    else:
        rc+=1
ans=min(lo,lc)+min(ro,rc)
print(ans)