def check(st,x):
    count=0
    for i in range(0,len(st)-1):
        if(st[i]!=st[i+1]):
            count=count+1
    if(count==x):
        return 1
    else:
        return 0
a,b,x=map(int,input().split())
s=''
curr='0'
if(min(a,b)==a):
    curr='1'
else:
    curr='0'
if(a==b):
    curr='0'
count=0
for i in range(0,a+b):
    if(count!=x):
        s=s+curr
        if(curr=='0'):
            a=a-1
            curr='1'
        else:
            b=b-1
            curr='0'
        count=count+1
if(s[len(s)-1]=='0'):
    for j in range(0,a):
        s=s+'0'
    for j in range(0,b):
        s=s+'1'
else:
    for j in range(0,b):
        s=s+'1'
    for j in range(0,a):
        s=s+'0'
'''
if(check(s,x)):
    print(s)
else:
    st=''
    for i in range(0,len(s)):
        if(s[i]=='0'):
            st=st+'1'
        else:
            st=st+'0'
    print(st)
'''
print(s)