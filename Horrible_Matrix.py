A=[[0,1,0],[1,1,1]]

def f(A):
    ans=0
    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            print(A[i][j],end=' ')
        print()
    for i in range(0,len(A)):
        t=A[i]
        t.sort()
        arr=[]
        if(t[0]==0 and t[len(t)-1]==1):
            return("NO")
        for j in range(0,len(A)):
            arr.append(A[i][j])
        arr.sort()
        if(arr[0]==0 and arr[len(arr)-1]==1):
            return("NO")
    return("YES")
print(f(A))