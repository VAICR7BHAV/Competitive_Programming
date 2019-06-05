from sys import stdin,stdout
t=int(stdin.readline())
while(t>0):
    n,m=map(int,stdin.readline().split())
    arr=[]
    for i in range(0,n):
        s=input()
        arr.append(s)
    ans="YES"
    for i in range(0,m):
        if(arr[0][i]=='#' and n>2):
            try:
                if(arr[0][i-1]=='#'):
                    ans="NO"
                    break
                else:
                    ans="YES"
            except:
                ans="YES"
                asdf=0
            try:
                if(arr[0][i-2]=='#'):
                    ans="NO"
                    break
                else:
                    ans="YES"
            except:
                ans="YES"
                asfa=0
            try:
                if(arr[0][i+1]=='#'):
                    ans="NO"
                    break
                else:
                    ans="YES"
            except:
                sdfsdf=0
            try:
                if(arr[0][i+2]=='#'):
                    ans="NO"
                    break
                else:
                    ans="YES"
            except:
                ans="YES"
                sf=0
        if (arr[0][i] == '#' and n ==2):
            ans="NO"
            break
    print(ans)
    t-=1