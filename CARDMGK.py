from sys import stdin,stdout
from collections import Counter
t=int(stdin.readline())
while(t>0):
    n = int(stdin.readline())
    A=[int(i) for i in stdin.readline().split()]
    s=''
    for i in range(1,len(A)):
        if(A[i]-A[i-1]>=0):
            s+='I'
        else:
            s+='D'
    curr=s[0]
    all=True
    ans=''
    d=Counter(s)
    print(s)
    if(len(s)==1):
        ans="YES"
    elif(d['I']==0):
        ans="NO"
    else:
        sd=[0]*len(s)
        '''
        for i in range(1,len(s)):
            if(s[i]!=curr and all):
                all=False
                ans="YES"
            elif(s[i]==curr):
                ans="YES"
            else:
                ans="NO"
                break
            curr=s[i]
        '''
        start=True
        for i in range(0,len(s)):
            if(s[i]=='I'):
                sd[i]=0
                start=True
            else:
                if(s[i]=='D' and start):
                    sd[i]=1
                    start=False
                elif(s[i]=='D'):
                    sd[i]=0
        print(sd)
    stdout.write((ans)+'\n')
    t-=1
