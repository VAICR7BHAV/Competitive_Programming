from collections import Counter
from sys import stdin,stdout
t=int(input())
for j in range(0,t):
    s=input()
    d=Counter(s)
    #print(d)
    li=[]
    for key in d:
	    li.append(d[key])
    li.sort()
    #print(li)
    flag=0
    if(len(d)>=3):
        for i in range(0,len(li)-2):
            if(li[i+2]==li[i+1]+li[i]):
                flag=1
            else:
                flag=0
                break
    if(len(d)<3):
        flag=1
    if(flag):
        stdout.write("Dynamic"+'\n')
    else:
        stdout.write("Not"+'\n')