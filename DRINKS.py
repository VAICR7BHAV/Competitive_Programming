n=int(input())
p=[int(i) for i in input().split()]
tot=n*100
ava=sum(p)
ans=(ava/tot)*100
print(ans)