n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
q=[int(i) for i in input().split()]
ans_vasya=[0]*100001
ans_petya=[0]*100001
for i in range(0,n):
    ans_vasya[a[i]]=i+1
    ans_petya[a[i]]=n-i
an_vas=0
an_pet=0
for i in range(0,m):
    an_vas+=ans_vasya[q[i]]
    an_pet+=ans_petya[q[i]]
print(an_vas,an_pet)