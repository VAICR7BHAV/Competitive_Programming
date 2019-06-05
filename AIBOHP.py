def f(s):
    global s1
    global s2
    s1=s
    s2=s1[::-1]
    n=len(s1)
    l1=len(s1)
    l2=l1
    dp=[[-1 for _ in range(n)] for _ in range(n)]
    def lcs(i,j):
        global s1
        global s2
        if(i<0 or j<0):
            return 0
        if(dp[i][j]!=-1):
            return (dp[i][j])
        if(s1[i]==s2[j]):
            dp[i][j]=1+lcs(i-1,j-1)
        else:
            dp[i][j]= max(lcs(i-1, j), lcs(i, j-1))
        return(dp[i][j])
    return(lcs(l1-1,l2-1))
t=int(input())
for i in range(0,t):
    s=input()
    val=len(s)-f(s)
    print(val)