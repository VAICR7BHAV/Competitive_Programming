from sys import stdin,stdout
from collections import Counter
def check(n):
    v1=Counter(n)
    try:
        if(v1['3']>=3):
            return True
        else:
            return False
    except:
        return False
t=int(stdin.readline())
for k in range(0,t):
    n=int(stdin.readline())
    n+=1
    while (True):
        if (check(str(n))):
            stdout.write(str(n)+'\n')
            break
        else:
            n += 1