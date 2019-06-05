from sys import stdin,stdout
from collections import Counter
t=int(stdin.readline())
while(t>0):
    #n=int(stdin.readline())
    for n in range(27,37):
        oneto26=[[0,0,1],[1,0,0],[1,0,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]
        rem=n%26
        quo=n//26
        val=2**quo
        if(rem==0):
            val=2**(quo-1)
        ans=oneto26[rem]
        for i in range(0,len(ans)):
                stdout.write(str(val*ans[i])+' ')
        stdout.write('\n')
    t-=1