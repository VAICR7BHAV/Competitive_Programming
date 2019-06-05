n,m=map(int,input().split())
s=[]
for i in range(0,n):
    s.append(input())
str='B'
row=0
col=0
while(len(str)<=m):
    for i in range(0,n):
        pos=s[i].find(str)
        #print(pos)
        if(pos>=0):
            flag=1
            print(str)
            if(i+len(str)<n):
                for j in range(i+1,i+len(str)):
                    if(s[j].find(str)==pos):
                        flag=1
                    else:
                        flag=0
                        break
            if(flag!=0):
                row=i+len(str)//2+1
                col=pos+len(str)//2+1
    str=str+'BB'
print(row,col)