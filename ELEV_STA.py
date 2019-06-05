import math
from sys import stdin,stdout
x,y,z,t1,t2,t3=map(int,stdin.readline().split())
ttbs=abs((y-x))*t1
ttbl=abs((z-x))*t2+2*t3+abs((y-x))*t2+t3
#print(ttbs,ttbl)
if(ttbl<=ttbs):
    stdout.write("YES")
else:
    stdout.write("NO")