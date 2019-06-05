from sys import stdin,stdout
def left(arr,n,m):
    num1r=[]
    for i in range(0,n):
        count=0
        for j in range(0,m):
            if(arr[i][j]=='1'):
                count+=1
        num1r.append(count)
    for i in range(0,n):
        list=[]
        for j in range(0,m):
            if(j<num1r[i]):
                list.append('1')
            else:
                list.append('0')
        arr[i]=list
    return arr
def right(arr,n,m):
    num1r = []
    for i in range(0, n):
        count = 0
        for j in range(0, m):
            if (arr[i][j] == '1'):
                count += 1
        num1r.append(count)
    for i in range(0,n):
        list=[]
        for j in range(0,m):
            if(j<m-num1r[i]):
                list.append('0')
            else:
                list.append('1')
        arr[i]=list
    return arr
def up(arr,n,m):
    num1c=[]
    for i in range(0,m):
        count=0
        for j in range(0,n):
            if(arr[j][i]=='1'):
                count+=1
        num1c.append(count)
    #print(num1c)
    for i in range(0,m):
        for j in range(0,n):
            if(j<num1c[i]):
                arr[j][i]='1'
            else:
                arr[j][i]='0'
    return arr
def down(arr,n,m):
    num1c = []
    for i in range(0, m):
        count = 0
        for j in range(0, n):
            if (arr[j][i] == '1'):
                count += 1
        num1c.append(count)
    #print(num1c)
    for i in range(0, m):
        for j in range(0, n):
            if (j <n-num1c[i]):
                arr[j][i] = '0'
            else:
                arr[j][i] = '1'
    return arr
t=int(input())
for i in range(0,t):
    n,m=map(int,input().split())
    grid=[]
    for j in range(0,n):
        grid.append(list(input()))
    s=input()
    first=0
    lastlr=0
    lastud=0
    '''
    for j in range(0,len(s)):
        if(s[j]=='L' or s[j]=='R'):
            lastlr=j
        else:
            lastud=j
    '''
    FL=s.rfind('L')
    FR=s.rfind('R')
    FD=s.rfind('D')
    FU=s.rfind('U')
    lastlr=max(FL,FR)
    lastud=max(FU,FD)
    if(lastlr==-1):
        lastlr=0
    if(lastud==-1):
        lastud=0
    if(s[0]=='L'):
        grid=left(grid,n,m)
    elif(s[0]=='R'):
        grid=right(grid,n,m)
    elif(s[0]=='U'):
        grid=up(grid,n,m)
    else:
        grid=down(grid,n,m)
    sl=min(lastlr,lastud)
    l=max(lastlr,lastud)
    if(sl!=0):
        if (s[sl] == 'L'):
            grid = left(grid, n, m)
        elif (s[sl] == 'R'):
            grid = right(grid, n, m)
        elif (s[sl] == 'U'):
            grid = up(grid, n, m)
        else:
            grid = down(grid, n, m)
    if(l!=0):
        if (s[l] == 'L'):
            grid = left(grid, n, m)
        elif (s[l] == 'R'):
            grid = right(grid, n, m)
        elif (s[l] == 'U'):
            grid = up(grid, n, m)
        else:
            grid = down(grid, n, m)
    '''
    for j in range(0,len(s)):
        if(s[j]=='L' and j-1>=0 and s[j-1]!='L'):
            grid=left(grid,n,m)
        elif(s[j]=='R'and j-1>=0 and s[j-1]!='R'):
            grid=right(grid,n,m)
        elif(s[j]=='D'and j-1>=0 and s[j-1]!='D'):
            grid=down(grid,n,m)
        elif(s[j]=='U'and j-1>=0 and s[j-1]!='U'):
            grid=up(grid,n,m)
    '''
    for j in range(0,n):
        for k in range(0,m):
            print(grid[j][k],end='')
        print()