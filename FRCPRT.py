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
t=int(raw_input())
for i in range(0,t):
    n,m=map(int,raw_input().split())
    grid=[]
    for j in range(0,n):
        grid.append(list(raw_input()))
    s=raw_input()
    for j in range(0,len(s)):
        if(s[j]=='L' and j-1>=0 and s[j-1]!='L'):
            grid=left(grid,n,m)
        elif(s[j]=='R'and j-1>=0 and s[j-1]!='R'):
            grid=right(grid,n,m)
        elif(s[j]=='D'and j-1>=0 and s[j-1]!='D'):
            grid=down(grid,n,m)
        elif(s[j]=='U'and j-1>=0 and s[j-1]!='U'):
            grid=up(grid,n,m)
    for j in range(0,n):
        for k in range(0,m):
            print(grid[j][k],end='')
        print()