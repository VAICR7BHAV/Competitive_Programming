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
        return And
t=int(stdin.readline())
while(t>0):
    n,q=map(int,stdin.readline().split())
    A=[int(i) for i in stdin.readline().split()]
    and_cal = [[-1 for x in range(n)] for y in range(n)]
    for i in range(0,q):
        count = 0
        arr=[]
        L,R=map(int,stdin.readline().split())
        k=L-1
        ini=[]
        while (k != R):
            for j in range(k,R):
                ini.append((k,j))
                arr.append(A[k:j+1])
            k+=1
        for i in range(0,len(arr)):
            And = 0
            if (and_cal[ini[i][0]][ini[i][1]] != -1):
                And = and_cal[ini[i][0]][ini[i][1]]
            else:
                And = cal_bit_and(arr[i])
            and_cal[ini[i][0]][ini[i][1]] = And
            And=cal_bit_and(arr[i])
            if(check_per_square(And)):
                count+=1
        stdout.write(str(count)+'\n')
    t-=1