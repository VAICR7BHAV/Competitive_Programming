from sys import stdin,stdout
def check_per_square(n):
    a=n**0.5
    if ((int(a) ** 2) == n):
        return True
    else:
        return False
def cal_bit_and(arr):
    And=arr[0]
    if(len(arr)==1):
        return And
    else:
        for i in range(1,len(arr)):
            And=And & arr[i]
            if(And==0):
                break
        return And
def ans_calc(L,R,A,and_cal):
    if(R<L):
        return -1
    k=L-1
    count=0
    arr=[]
    ini=[]
    while (k != R):
        for j in range(k, R):
            # print(A[k:j+1])
            arr.append(A[k:j + 1])
            ini.append((k,j))
        k += 1
    ##print(arr)
    #print(ini)
    for i in range(0, len(arr)):
        And=0
        if(and_cal[ini[i][0]][ini[i][1]]!=-1):
            And=and_cal[ini[i][0]][ini[i][1]]
        else:
            And = cal_bit_and(arr[i])
        and_cal[ini[i][0]][ini[i][1]]=And
        # print(arr[i],And)
        if (check_per_square(And)):
            count += 1
    return count
t=int(stdin.readline())
while(t>0):
    n,q=map(int,stdin.readline().split())
    A=[int(i) for i in stdin.readline().split()]
    ans=[[-1 for x in range(n)] for y in range(n)]
    #print(ans)
    #print(ans[0][2])
    and_cal=[[-1 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            ans[i][j]=ans_calc(i+1,j+1,A,and_cal)
    for i in range(0,q):
        L,R=map(int,stdin.readline().split())
        print(ans[L-1][R-1])
    t-=1