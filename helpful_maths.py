a=[int(i) for i in input().split('+')]
a.sort()
for i in range(0,len(a)):
    if(i!=len(a)-1):
        print(str(a[i])+'+',end='')
    else:
        print(str(a[i]),end='')