import math
def lcm(x, y):
   lcm = (x*y)//math.gcd(x,y)
   return lcm
k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
'''
l1=lcm(k,l)
l2=lcm(k,m)
l3=lcm(k,n)
ans=d//k+d//l+d//m+d//n-d//l1-d//l2-d//l3
print(ans)
'''
arr=[]
for i in range(1,d+1):
   if(i%k==0 or i%l==0 or i%m==0 or i%n==0):
      arr.append(i)
se=set(arr)
print(len(se))