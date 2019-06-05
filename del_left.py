from sys import stdin,stdout
s=input()
t=input()
ans=0
delt=0
pos=0
cond=False
for i in range(0,len(t)):
    pos=s.find(t[i:])
    if(pos!=-1 and s[pos:]==t[i:]):
        delt=i
        cond=True
        break
#print(pos,delt)
if(cond):
    ans=ans+delt+pos
else:
    ans=len(s)+len(t)
stdout.write(str(ans)+'\n')