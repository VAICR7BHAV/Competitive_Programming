from sys import stdin,stdout
from collections import Counter
t=int(stdin.readline())
while(t>0):
    n=int(stdin.readline())
    bit=[0]
    nibble=[]
    byte=[]
    for i in range(0,n):
        for j in range(0,len(bit)):
            if(bit[j]==2):
                nibble.append(0)
                bit[j]=-1
            elif(bit[j]!=-1):
                bit[j]+=1
        for j in range(0,len(nibble)):
            if(nibble[j]==8):
                byte.append(0)
                nibble[j]=-1
            elif(nibble[j]!=-1):
                nibble[j]+=1
        for j in range(0,len(byte)):
            if(byte[j]==16):
                bit.append(0)
                bit.append(0)
                byte[j]=-1
            elif(byte[j]!=-1):
                byte[j]+=1
    d1=Counter(bit)
    d2=Counter(nibble)
    d3=Counter(byte)
    ans=str(len(bit)-d1[-1])+' '+str(len(nibble)-d2[-1])+' '+str(len(byte)-d3[-1])
    #print(len(bit)-d1[-1],len(nibble)-d2[-1],len(byte)-d3[-1])
    stdout.write(ans+'\n')
    t-=1