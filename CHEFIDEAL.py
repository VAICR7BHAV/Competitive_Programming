from collections import Counter
import sys
arr=[]
print(1)
sys.stdout.flush()
arr.append(1)
inp=int(input())
arr.append(inp)
d=Counter(arr)
if(d[2]!=1):
    print(2)
    sys.stdout.flush()
else:
    print(3)
    sys.stdout.flush()